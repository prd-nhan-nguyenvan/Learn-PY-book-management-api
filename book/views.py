from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from book.models import Book, Author
from book.serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        if isinstance(data, list):
            serializer = BookSerializer(data=data, many=True)
        else:
            serializer = BookSerializer(data=data)

        # Validate and save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
