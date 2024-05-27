from posts.models import Post
from questions.models import Qustion
from answers.models import Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qustion
        fields = ['id','question']

class AnswerSerializer(serializers.ModelSerializer):
    options = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ['id','answer','options','url']

class PostSerializer(serializers.ModelSerializer):
    #default_response = serializers.StringRelatedField(many=True)
    default_response = QuestionSerializer(many=True, read_only=True)
    bot_response = AnswerSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['message', 'default_response', 'bot_response', 'created_at', 'updated_at']


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','message', 'default_response', 'bot_response','uid', 'created_at', 'updated_at']
