from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('camera', views.camera, name='camera'),
    path('profile', views.profile, name='profile'),
]
