from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=150)
    born_date = models.CharField(max_length=150)
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.CharField(max_length=150)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, default=None, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
