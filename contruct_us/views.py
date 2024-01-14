from django.shortcuts import render
from rest_framework import viewsets
from. import models
from. import serializers

# Create your views here.
class ContractUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContructUs.objects.all()
    serializer_class=serializers.ContructUsSeeializer
