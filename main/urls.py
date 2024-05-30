from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='home'),
    path('user', views.user, name='user'),
    path('about', views.about, name='about'),
    path('', views.search, name='search')


]

