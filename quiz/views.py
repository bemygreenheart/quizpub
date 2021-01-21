from django.shortcuts import render
from .serializers import QuestionSerializer, OptionSerializer, QuizSerializer, CommentSerializer
from .models import Quiz, Question, Option, Comment
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer