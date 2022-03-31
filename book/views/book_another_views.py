from django.shortcuts import render

def ending(request):
    return render(request, 'book/endingBook.html')

def TopBook(request):
    return render(request, "book/topbook.html")