from django.urls import include, path

urlpatterns = [
    path("api/auth/", include("users.urls")),
    path("api/", include("book.urls")),
]
