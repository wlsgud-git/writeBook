from os import access
from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from common.models import Users
from ..models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from writeBook.settings import SECRET_KEY
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import jwt, datetime
from writeBook.settings import SECRET_KEY, JWT_ALGORITHM

# @login_required(login_url="common:login")
@permission_classes([AllowAny])
def index(request):
    if request.method == "POST":
        access_token = request.headers.get('Authorization')

        decoded = jwt.decode(access_token, SECRET_KEY, JWT_ALGORITHM)
    return render(request, 'book/index.html')