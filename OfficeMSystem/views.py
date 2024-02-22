from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, TaskDetails
from .serializers import MessageSerializer, TaskDetailsSerializer



class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class =  MessageSerializer    
    
class TaskDetailsViewset(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class =  TaskDetailsSerializer

