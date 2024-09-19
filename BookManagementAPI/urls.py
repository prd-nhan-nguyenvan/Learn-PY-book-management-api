from django.urls import path, include

urlpatterns = [
    path('api/user',include('users.urls')),
    path('api/', include('book.urls')),
]