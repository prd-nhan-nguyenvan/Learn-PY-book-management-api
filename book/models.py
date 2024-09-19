from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    language = models.CharField(max_length=100, default='English')
    link = models.URLField(max_length=500, null=True, blank=True)
    pages = models.IntegerField(default=0)
    publication_date = models.DateField(default='1970-01-01')

    def __str__(self):
        return self.title
