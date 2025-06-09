from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):
    STATUS = [
        ('todo','To Do'),
        ('in_progress','In Progress'),
        ('done','Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS,default='todo')
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title