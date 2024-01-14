from rest_framework import serializers
from. import models

class DoctorSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    designation=serializers.StringRelatedField(many=True)
    specialization=serializers.StringRelatedField(many=True)
    availableTime=serializers.StringRelatedField(many=True)
    class Meta:
        model=models.Doctor
        fields='__all__'
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AvailableTime
        fields='__all__'
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Designation
        fields='__all__'
class SpecializaionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Specializaion
        fields='__all__'
class ReviweSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Reviwe
        fields='__all__'