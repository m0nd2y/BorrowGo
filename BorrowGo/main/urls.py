from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('postcreate', views.postcreate, name='main_postcreate'),
    path('postcreate/create', views.postcreate_create, name = 'main_posetcreate_create'),
    path('postdetail/<str:post_id>', views.postdetail, name = 'main_postdetail'),
    path('postdetail/<str:post_id>/comment', views.postcomment, name = 'main_postcomment'),
    path('postdetail/<str:post_id>/comment/create', views.postcomment_create, name = 'main_postcomment_create'),
    path('postdetail/<str:post_id>/commentDetail/<str:comment_id>', views.commentdetail, name = 'main_commentdetail'),
    path('signup', views.signup, name='main_signup'),
    path('signup/join', views.join, name='main_join'),
    path('signin', views.signin, name='main_signin'),
    path('signin/login', views.login, name='main_login'),
    path('result', views.result, name='main_result'),
    path('logout', views.logout, name='main_logout')
]