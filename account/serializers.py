from rest_framework.serializers import ModelSerializer
from django.conf.global_settings import AUTH_USER_MODEL

class UserSerializer(ModelSerializer):
  class Meta:
    model = AUTH_USER_MODEL
    fields = ['id', 'username', 'email', 'first_name', 'last_name']
    