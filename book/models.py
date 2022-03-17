from pyexpat import model
from venv import create
from django.db import models
from common.models import Users

# Create your models here.

class Books(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateField()

    like_book = models.ManyToManyField(Users, related_name='book_like', blank=True)

class Comments(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()
    like_comment = models.ManyToManyField(Users, related_name='comment_like', blank=True)
