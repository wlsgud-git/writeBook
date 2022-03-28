from django.shortcuts import redirect, render
from common.models import Users
from django.contrib import auth
from rest_framework.authtoken.models import Token

def login(request):
    return render(request, 'common/login.html')  

def logout(request):
    auth.logout(request)
    return redirect("common:login")