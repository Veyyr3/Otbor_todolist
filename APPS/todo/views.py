from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# seria
from .serializers import TaskSerializer

# models
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer