from django.shortcuts import render
from common.models import Users
from ..models import Books

def index(request):
    print(request)
    profile_image = request.user.profile_image
    username = request.user.username
    books = Books.objects.all()
    return render(request, 'book/index.html', {'profile_image': profile_image, 'username':username, 'books':books})

def Detail(request):
    return render(request, 'book/detail.html')