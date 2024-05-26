
from . import views


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.track_order, name='track_order')
]

