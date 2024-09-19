from rest_framework import serializers
from datetime import datetime
from rest_framework.validators import UniqueTogetherValidator

from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'nationality']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())  # Reference existing authors by ID

    class Meta:
        model = Book
        fields = ['author', 'language', 'link', 'pages', 'title', 'publication_date']
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['author', 'title']
            )
        ]

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
