from django.shortcuts import render
from common.models import Users
from ..models import Books
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# @login_required(login_url="common:login")
def index(request):
    profile_image = request.user.profile_image
    username = request.user.username
    books = Books.objects.all()
    return render(request, 'book/index.html', {'profile_image': profile_image, 'username':username, 'books':books})

def practice(request):
    if request.method == "POST":
        im = request.FILES.get('upload')
        print(im)
    return render(request, 'practice.html')