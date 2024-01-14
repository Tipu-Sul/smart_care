# from serializers import Serializer
from rest_framework import serializers
from. import models

class ContructUsSeeializer(serializers.ModelSerializer):
    class Meta:
        model=models.ContructUs
        fields="__all__"
