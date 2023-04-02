from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Profile
from .serializer import ProfileSerializer
from Home.CustomPermision import isOwnorOrReadOnly


class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [isOwnorOrReadOnly]
    