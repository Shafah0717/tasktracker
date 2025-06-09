from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    class meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']

