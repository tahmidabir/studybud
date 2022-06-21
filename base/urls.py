from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # see information about a specific room passing a dynamic value

    path('room/<str:pk>/', views.room, name='room'),

]
