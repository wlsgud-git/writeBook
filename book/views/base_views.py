from django.shortcuts import render
from common.models import Users
from ..models import Books, Slider
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from writeBook.settings import SECRET_KEY

# @login_required(login_url="common:login")
def index(request):
    user = jwt.decode(request.COOKIES['jwt'][2:-1], SECRET_KEY, algorithms=["HS256"])
    return render(request, 'book/index.html')

def practice(request):
    if request.method == "POST":
        im = request.FILES.get('upload')
        print(im)
    return render(request, 'practice.html')