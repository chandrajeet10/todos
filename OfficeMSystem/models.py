from django.db import models

class User(models.Model):
    email= models.EmailField(unique=True)
    username= models.CharField(max_length=100)

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    due_date  = models.DateField()
    priority_level = models.IntegerField()
    
class TaskDetails(models.Model):
    task= models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_to=  models.ManyToManyField('auth.User')

    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)