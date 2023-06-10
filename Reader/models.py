from django.db import models

class Reader(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, default=' ')
    email = models.EmailField()

    def __str__(self):
        return self.name
