from django.shortcuts import redirect, render

def userEdit(request, email):
    if request.method == "POST":
        print(request.FILES['profile_image'])
    return render(request, 'common/userEdit.html')

def pwFind(request, pk):
    return render(request, 'common/pwFind.html')

def library(request, email):
    return render(request, 'common/library.html')