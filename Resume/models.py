from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=200)
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=1000)

    def __str_(self):
        return self.Subject
