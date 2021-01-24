from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

def quiz_image_path(instance, filename):
  return 'quiz/{}/{}'.format(instance.id, filename)

class Category(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  slug = models.SlugField()

class Quiz(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(null=True)
  owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
  image = models.ImageField(null=True, upload_to=quiz_image_path)
  created_at = models.DateTimeField("created time",auto_now_add=True)
  is_published = models.BooleanField( default=True)
  publish_date = models.DateTimeField(null=True)
  comments = models.ManyToManyField(AUTH_USER_MODEL, through="Comment", related_name='my_comments')
  favourites = models.ManyToManyField(AUTH_USER_MODEL, related_name="my_favourites")
  categories = models.ManyToManyField(Category, related_name="quizes")

def question_image_path(instance, filename):
  return 'options/{}/{}'.format(instance.id, filename)

class Question(models.Model):
  text = models.TextField()
  has_multiple_answers = models.BooleanField(default=False)
  image = models.ImageField(null=True, upload_to = question_image_path)
  quiz = models.ForeignKey(Quiz, null=True, on_delete=models.CASCADE, related_name='questions')

class Option(models.Model):
  text = models.CharField(max_length=400)
  is_answer = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')

class Comment(models.Model):
  owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

class QuizAttempt(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
  score = models.FloatField(default=0)
  attempt_time = models.DateTimeField(auto_now_add=True)
  
