from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
class UserViewSet(viewsets.ViewSet):

  def list(self, request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk = None ):
    queryset = User.objects.all()
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    