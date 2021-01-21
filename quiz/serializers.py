from rest_framework import serializers

from .models import Option, Question, Quiz, Comment, Category

class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    fields = ['text', 'is_answer']

  def create(self, validated_data):
    return Option.objects.create(**validated_data)

  def update(self,instance ,validated_data):
    instance.email = validated_data.get('text', instance.email)
    instance.is_answer = validated_data.get('is_answer', instance.is_answer)
    instance.save()
    return instance

class QuestionSerializer(serializers.ModelSerializer):
  options = OptionSerializer(many = True)

  class Meta:
    model = Question
    fields = ['text', 'has_multipe_answers', 'options','image']

  def create(self, validated_data):
    options_data = validated_data.pop('options')
    question = Question.objects.create(**validated_data)
    for option_data in options_data:
      Option.objects.create(**option_data, question=question)
    return question

  def update(self, instance, validated_data):
    pass

class CommentSerializer(serializers.ModelSerializer):

  username = serializers.CharField(source='owner.username', read_only=True)
  class Meta:
    model = Comment
    fields = ['text', 'created_at']

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ['id','title', 'description', 'slug']


class QuizSerializer(serializers.ModelSerializer):
  questions = QuestionSerializer(many = True)
  username = serializers.CharField(source='owner.username', read_only=True)
  comments = CommentSerializer(many = True, read_only=True)
  categories = CategorySerializer(many=True)
  class Meta:
    model = Quiz
    fields = ['title', 'description', 'image', 'created_at', 'is_published', 'publish_date', 'comments']

  def create(self, validated_data):
    questions_data = validated_data.pop('questions')
    quiz = Quiz.objects.create()
    for question_data in questions_data:
      Question.objects.create(question)