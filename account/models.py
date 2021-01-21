from django.db import models 

from django.conf.global_settings import AUTH_USER_MODEL

def user_directory_path(instance, filename):
  return f"user_{instance.user.id}/{filename}"

class Profile(models.Model):
  user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
  description = models.TextField(null=True)
  photo = models.ImageField('profile photo', null=True, upload_to = user_directory_path)


  def __str__(self):
    return self.user.username