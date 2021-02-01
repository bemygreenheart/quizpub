from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet
from django.views.generic import TemplateView

from rest_framework.authtoken import views as drf_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
  path('auth/', include('rest_framework.urls'), name='auth'),
  path('', TemplateView.as_view(template_name="index.html"), name="home")
]+router.urls