from django.http import HttpRequest
from django.shortcuts import redirect, render
from common.models import Users
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'common/login.html')  

def logout(request):
    auth.logout(request)
    return redirect("common:login")