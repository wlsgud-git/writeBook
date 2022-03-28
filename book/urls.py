from django.urls import path
from .views import base_views
from .api import book_api, comment_api

app_name = "book"

urlpatterns = [
    # api
    path('booklist-api/', book_api.BookList.as_view()),
    path('book-detail/api/', book_api.BookDetail.as_view()), 
    path('commentlist-api/', comment_api.CommentsList.as_view()),
    path('<int:pk>/api/', comment_api.CommentDetail.as_view()),
    # base_views.py
    path('', base_views.index, name = 'index'),
    path('detail/', base_views.Detail, name="Detail")
]