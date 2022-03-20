from django.shortcuts import redirect, render

def signup(request):
    return render(request, 'common/signup.html')