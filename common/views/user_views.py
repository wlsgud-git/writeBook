from django.shortcuts import redirect, render

def userEdit(request, pk):
    return render(request, 'common/userEdit.html')

def pwFind(request, pk):
    return render(request, 'common/pwFind.html')