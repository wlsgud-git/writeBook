from django.shortcuts import render

def searchResult(request):
    return render(request, 'book/searchResult.html')
