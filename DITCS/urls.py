from django.contrib import admin
from django.urls import path, include
from traffic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('traffic.urls')),
]
