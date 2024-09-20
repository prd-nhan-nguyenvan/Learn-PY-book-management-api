from django.urls import include, path
from rest_framework.routers import DefaultRouter

from book.views import AuthorViewSet, BookListLanguage, BookViewSet

router = DefaultRouter()
router.register(viewset=AuthorViewSet, prefix="authors")
router.register(viewset=BookViewSet, prefix="books")

urlpatterns = [
    path("", include(router.urls), name="api"),
    path("books/<str:language>", BookListLanguage.as_view(), name="book-list-language"),
]
