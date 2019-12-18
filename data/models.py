from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
