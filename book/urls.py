from django.urls import path
from .views import base_views, book_views, book_another_views
from .api import book_api, comment_api

app_name = "book"

urlpatterns = [
    # api
    path('slide-image/api/', book_api.SliderImageList.as_view()),
    # base_views.py
    path('', base_views.index, name = 'index'),
    # book_veiws.py
    path('result/', book_views.searchResult, name = 'searchResult'),
    # book_another_views
    path('ending/', book_another_views.ending, name = "ending"),
    path('top100/', book_another_views.TopBook, name = "topbook"),
]