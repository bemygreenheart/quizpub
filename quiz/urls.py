from django.urls import include
from rest_framework import routers

from .views import QuestionViewSet, QuizViewSet, CategoryViewSet, OptionViewSet

router = routers.DefaultRouter()

router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'quizes', QuizViewSet, basename='quiz')
router.register(r'options', OptionViewSet, basename='option')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls 

