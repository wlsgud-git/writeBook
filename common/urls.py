from django.urls import path
from .api import user_api, signup_api, login_api
from .views import user_views, login_views,signup_views

app_name = "common"

urlpatterns = [
    # api
    path('users/api/', user_api.UserList.as_view()),
    path('login/api/', login_api.LoginApi.as_view()),
    path('<str:email>/api/', user_api.UserDetail.as_view()),
    path('resister/', signup_api.ResisterApi.as_view()),
    path('access_token/verify/', login_api.AccessTokenVeridate.as_view()),
    # login
    path('login/', login_views.login, name = "login"),
    # signup
    path('signup/', signup_views.signup, name='signup'),
    # user_views
    path('<str:email>/', user_views.userEdit, name = "userEdit"),
    path('user/<int:pk>/pwFind/', user_views.pwFind, name="pwFind"),
    path('<str:email>/library/', user_views.library, name="library"),
]

