from rest_framework import serializers
from datetime import datetime
from rest_framework.validators import UniqueTogetherValidator

from .models import Book, Author

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books  = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)


    class Meta:
        model = Author
        fields = ['id', 'url', 'name', 'birth_date', 'nationality', 'books']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.SerializerMethodField()
    author_url = serializers.HyperlinkedIdentityField(view_name='author-detail')  # Reference existing authors by ID
    class Meta:
        model = Book
        fields = ['url', 'id','author_name', 'language', 'link', 'pages', 'title', 'publication_date', 'author_url']
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['author', 'title']
            )
        ]

    def get_author_name(self, obj):
        return obj.author.name  # Assuming the Author model has a 'name' field

    # Custom validation for the publication_date field
    def validate_publication_date(self, value):
        if value < datetime(1970, 1, 1).date():
            raise serializers.ValidationError("The publication date must be after 1970.")
        return value

    # No need to handle author creation/updating in the `create` and `update` methods
    # as author is now referenced by ID
    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
