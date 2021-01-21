from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Option, Question, Quiz, Comment, Category

class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    fields = ['id', 'text', 'is_answer']

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
    fields = ['id','text', 'has_multiple_answers', 'options','image']

  def create(self, validated_data):
    options_data = validated_data.pop('options')
    question = Question.objects.create(**validated_data)
    for option_data in options_data:
      Option.objects.create(**option_data, question=question)
    return question

# Each question is updated individually to minimize network traffic
  def update(self, instance, validated_data):
    options_data = validated_data.pop('options')
    instance = validated_data.get("text", instance.text)
    instance.has_multiple_answers = validated_data.get('has_multiple_answers', instance.has_multiple_answers)
    instance.image = validated_data.get('image', instance.image)
    for option_data in options_data:
      option = get_object_or_404(Option, pk=option.id)
      option.text = option_data.get('text', option.text)
      option.is_answer = option_data.get('is_answer', option.is_answer)
      option.save()

    instance.save()
    return instance

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
    fields = ['id','title', 'description', 'image', 'created_at', 'is_published', 'publish_date', 'comments']

# Quiz is created at once with all the data for questions in it
  def create(self, validated_data):
    questions_data = validated_data.pop('questions')
    quiz = Quiz.objects.create(**validated_data)
    for question_data in questions_data:
      options_data = question_data.pop('options')
      question = Question.objects.create(quiz = quiz, **question_data)
      for option_data in options_data:
        Option.objects.create(question = question, **option_data)

    return quiz

# Just updating the quiz only data
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.is_published = validated_data.get('is_published', instance.is_published)
    instance.publish_date = validated_data.get('publish_date', instance.publish_date)
    instance.image = validated_data.get('image', instance.image)
    return instance
