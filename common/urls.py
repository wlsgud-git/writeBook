from django.urls import path
from .api import user_api
from .views import user_views

app_name = "common"

urlpatterns = [
    # api
    path('users/api/', user_api.UserList.as_view()),
    path('user/<int:pk>/api/', user_api.UserDetail.as_view()),
    # user_views
    path('user/<int:pk>/profile-edit/', user_views.userEdit, name = "userEdit")
]

