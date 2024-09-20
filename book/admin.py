from django.contrib import admin

from book.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'country', 'language', 'link', 'pages', 'title', 'publication_date']
