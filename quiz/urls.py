from django.urls import include
from rest_framework import routers

from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
urlpatterns = router.urls 

