from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
]
