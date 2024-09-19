from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book import views
from book.views import AuthorViewSet, BookViewSet, BookListLanguage

router = DefaultRouter()
router.register(viewset=AuthorViewSet, prefix='authors')
router.register(viewset=BookViewSet, prefix='books')

urlpatterns = [
    path('', include(router.urls), name='api'),
    path('books/<str:language>', BookListLanguage.as_view(), name="book-list-language")
]