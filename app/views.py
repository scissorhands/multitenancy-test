from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# local imports
from . import serializers
from . import models

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)