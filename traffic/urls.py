from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'traffic', views.TrafficViewSet)
router.register(r'road', views.RoadViewSet)
router.register(r'light', views.LightViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('camera', views.camera, name='camera'),
    path('profile', views.profile, name='profile'),
    path('api/', include(router.urls)),
]
