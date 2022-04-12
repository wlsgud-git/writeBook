from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from flask_sqlalchemy import models_committed
from sqlalchemy import null

# Create your models here.

class Users(AbstractUser):    
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True, max_length=254)
    profile_image = models.ImageField(null = True, blank = True, upload_to= "images/", default="images/default-user.jpg")
    update_time = models.DateField(null = True, blank=True)
    nickname = models.CharField(max_length=20,null = True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

