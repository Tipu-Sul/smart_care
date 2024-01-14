from django.shortcuts import render
from rest_framework import viewsets
from. import models
from. import serializer
from rest_framework import filters,pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializer.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100

class DesignationViewSet(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializer.DesignationSerializer

class SecializationViewSet(viewsets.ModelViewSet):
    queryset=models.Specializaion.objects.all()
    serializer_class=serializer.SpecializaionSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Reviwe.objects.all()
    serializer_class=serializer.ReviweSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serializer.DoctorSerializer
    filter_backends=[filters.SearchFilter]
    pagination_class=DoctorPagination
    search_fields=['user__first_name', 'user__email','designation__name','specification__name']
