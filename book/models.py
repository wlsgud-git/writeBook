from pyexpat import model
from venv import create
from django.db import models
from common.models import Users
import datetime
# Create your models here.import datetime

DAYS_OF_WEEK = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ) 

class Slider(models.Model):
    slide_image = models.ImageField(blank= True, null = True, upload_to= "images/")
   
class Books(models.Model):   
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='book_author')
    thumbnail = models.ImageField(null = False, blank = False, upload_to= "images/",)
    like_count = models.ManyToManyField(Users, related_name='book_like', blank = True)
    making = models.BooleanField(default=True)
    create_day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

class Episode(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)