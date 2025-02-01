# from django.shortcuts import render
from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
