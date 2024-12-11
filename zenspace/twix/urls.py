from django.contrib import admin
from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('followers/<int:pk>', views.followers, name='followers'),
    path('follows/<int:pk>', views.follows, name='follows'),
    path('twix/', views.twix_list, name= 'twix_list'),
    path('create/', views.twix_create, name= 'twix_create'),
    path('twix/<int:twix_id>/edit/', views.twix_edit, name= 'twix_edit'),
    path('twix/<int:twix_id>/delete/', views.twix_delete, name='twix_delete'),
    path('register/', views.register, name='register'), 
    path('search/', views.search_view, name='search'),
    path('update_user/', views.update_user, name='update_user'),
    path('twix_like/<int:pk>', views.twix_like, name='twix_like'),
    path('twix/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow'),
    



    
   
]