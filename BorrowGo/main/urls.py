from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('signup', views.signup, name='main_signup'),
    path('signup/join', views.join, name='main_join'),
    path('signin', views.signin, name='main_signin'),
    path('signin/login', views.login, name='main_login'),
    path('loginFail', views.loginFail, name='main_loginFail'),
    path('result', views.result, name='main_result'),
    path('logout', views.logout, name='main_logout')
]