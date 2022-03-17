from django.shortcuts import redirect, render
from common.models import Users
from django.contrib import auth

# def login(request):
#     return render(request, 'common:login')  

# def logout(request):
#     auth.logout(request)
#     return redirect("common:login")