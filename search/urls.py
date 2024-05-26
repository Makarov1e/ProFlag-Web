from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_order, name='track_order')
]

