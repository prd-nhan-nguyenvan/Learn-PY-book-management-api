from rest_framework import status, viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Author, Book
from book.serializers import AuthorSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data

        if isinstance(data, list):
            serializer = BookSerializer(
                data=data, many=True, context={"request": request}
            )
        else:
            serializer = BookSerializer(data=data, context={"request": request})

        # Validate and save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListLanguage(APIView):

    def get(self, request, language):
        query_set = Book.objects.all().filter(language=language)
        serializer = BookSerializer(query_set, many=True, context={"request": request})
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Custom for add multi authors"""
        data = request.data

        if isinstance(data, list):
            serializer = AuthorSerializer(
                data=data, many=True, context={"request": request}
            )
        else:
            serializer = AuthorSerializer(data=data, context={"request": request})

        # Validate and save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
