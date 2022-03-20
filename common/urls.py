from django.urls import path
from .api import user_api
from .views import user_views, login_views,signup_views

app_name = "common"

urlpatterns = [
    # api
    path('users/api/', user_api.UserList.as_view()),
    path('user/<int:pk>/api/', user_api.UserDetail.as_view()),
    path('resister/', user_api.ResisterApi.as_view()),
    # login
    path('login/', login_views.login, name = "login"),
    # signup
    path('signup/', signup_views.signup, name='signup'),
    # user_views
    path('user/<int:pk>/profile-edit/', user_views.userEdit, name = "userEdit"),
    path('user/<int:pk>/pwFind/', user_views.pwFind, name="pwFind"),
]

