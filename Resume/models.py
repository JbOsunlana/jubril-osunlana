from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
