from django.shortcuts import render
from .serializers import QuestionSerializer, OptionSerializer, QuizSerializer, CommentSerializer, CategorySerializer
from .models import Quiz, Question, Option, Comment, Category
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class QuizViewSet(viewsets.ModelViewSet):
  queryset = Quiz.objects.filter(is_published=True)
  serializer_class = QuizSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class OptionViewSet(viewsets.ModelViewSet):
  serializer_class = OptionSerializer
  queryset = Option.objects.all()
