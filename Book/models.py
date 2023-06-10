from django.db import models
from Reader.models import Reader

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default=' ')
    publication_date = models.DateField(null=True)
    description = models.TextField()
    readers = models.ManyToManyField(Reader, related_name='books')

    def __str__(self):
        return self.title
