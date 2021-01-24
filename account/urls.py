from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet

from rest_framework.authtoken import views as drf_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [path('auth/', include('rest_framework.urls'), name='auth')]+router.urls