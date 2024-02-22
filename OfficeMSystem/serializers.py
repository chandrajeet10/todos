from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')

class TaskSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Task
        fields = ('id', ' title ', ' due_date', ' priority_level')

class TaskDetailsSerializer(serializers.ModelSerializer):    
    class Meta:
        model= TaskDetails
        fields = '__all__'       


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']        