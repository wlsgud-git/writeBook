from django.urls import path
from .views import base_views, book_views, book_another_views
from .api import book_api, comment_api

app_name = "book"

urlpatterns = [
    # api
    path('booklist-api/', book_api.BookList.as_view()),
    path('book-detail/api/', book_api.BookDetail.as_view()), 
    path('day-of-book/api/', book_api.DayOfBook.as_view()),
    path('commentlist-api/', comment_api.CommentsList.as_view()),
    path('<int:pk>/api/', comment_api.CommentDetail.as_view()),
    path('endbook-list/api/', book_api.EndBookList.as_view()),
    path('topbook-list/api/', book_api.TopBookList.as_view()),
    path('all-time-best-books/api/', book_api.AllTimeBestBook.as_view()),
    path('slide-image/api/', book_api.SliderImageList.as_view()),
    # base_views.py
    path('', base_views.index, name = 'index'),
    path('practice/', base_views.practice, name='practice'),
    # book_veiws.py
    path('result/', book_views.searchResult, name = 'searchResult'),
    # book_another_views
    path('ending/', book_another_views.ending, name = "ending"),
    path('top100/', book_another_views.TopBook, name = "topbook"),
]