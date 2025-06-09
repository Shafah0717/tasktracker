from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskViewSet(ModelViewSet):
        queryset = Task.objects.all()
        serializer_class = TaskSerializers
        permission_classes = [IsAuthenticated]

        def get_queryset(self):
                return self.queryset.filter(owner=self.request.user)
        def perform_create(self, serializer):
                serializer.save(owner=self.request.user)
