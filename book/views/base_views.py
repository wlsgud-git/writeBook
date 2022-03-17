from django.shortcuts import render
from common.models import Users

def index(request):
    profile_image = request.user.profile_image
    username = request.user.username
    return render(request, 'book/index.html', {'profile_image': profile_image, 'username':username})