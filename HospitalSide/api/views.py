from django.shortcuts import render
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from HospitalSide.models import Appointment, Doctor, Patient
from rest_framework.permissions import AllowAny
from .serializers import AppointmentSerializer, DoctorsSerializer, PatientCreateSerializer, PatientListSerializer
from django.views.decorators.csrf import csrf_exempt

class CreatePatientView(CreateAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientCreateSerializer
	
	permission_classes = [AllowAny]


class PatientListView(ListAPIView):
	queryset = Patient.objects.all() # all patients
	serializer_class = PatientListSerializer
	
	permission_classes = [AllowAny]

class GetDoctorsByDepartment(ListAPIView):
	permission_classes = [AllowAny]
	serializer_class = DoctorsSerializer 

	def get_queryset(self):
		data = self.request.headers
		return Doctor.objects.filter(department=data['department'])

