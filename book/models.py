from pyexpat import model
from venv import create
from django.db import models
from common.models import Users

# Create your models here.

DAYS_OF_WEEK = (
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
    ('sun', 'Sunday'),
)

class Books(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateField()
    create_day_of_week =  models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    thumbnail = models.ImageField(blank= True, null = True, upload_to= "images/")
    making = models.BooleanField(default=True)

    like_book = models.ManyToManyField(Users, related_name='book_like', blank=True)
    views_count = models.PositiveBigIntegerField(default=0)

class Comments(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()
    like_comment = models.ManyToManyField(Users, related_name='comment_like', blank=True)


class Slider(models.Model):
    slide_image = models.ImageField(blank= True, null = True, upload_to= "images/")