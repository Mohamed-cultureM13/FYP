from django.shortcuts import render
#from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from HospitalSide.models import Patient , Doctor #, Appointment
from rest_framework.permissions import AllowAny
from .serializers import PatientSerializer , DoctorSerializer #, AppointmentSerializer


# Create your views here.

class PatientAPIView(CreateAPIView):
	@api_view(['POST',])
	def patient_details(request):
		if request.method == 'POST':
			queryset = Patient.objects.all()
			serializer_class = PatientSerializer
			permission_classes = [AllowAny]
			patient_data == JSONParser().parse(request)
			patient_serializer = PatientSerializer(data=patient_data)
			if patient_serializer.is_valid():
			   patient_serializer.save()
			   return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def get_serializer_class(self):
		if self.request.method in ('POST',):
			return PatientSerializer
		return self.serializer_class
		
		
class DoctorAPIView(CreateAPIView):
	@api_view(['GET', 'POST'])
	def department_list(request):
		if request.method == 'GET':
			queryset = Doctor.objects.all()
			serializer_class = DoctorSerializer
			permission_classes = [AllowAny]
			user = request.query_params.get('user',None)
			if user is not None:
				queryset = queryset.filter(user__icontains=user)
				
			doctor_serializer = DoctorSerializer(queryset, many=True)
			return JsonResponse(doctor_serializer.data, safe=False)
			
		elif request.method == 'POST':
			department_data = JSONParser().parse(request)
			doctor_serializer =DoctorSerializer(data=department_data)
			if doctor_serializer.is_valid():
				doctor_serializer.save()
				return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED)
			return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def get_serializer_class(self):
		if self.request.method in ('GET','POST'):
			return DoctorSerializer
		return self.serializer_class							

'''class AppointmentAPIView(CreateAPIView):
	def doctor_list(request):
		if request.method == 'GET':
			doctors = Appointment.objects.all()
			serializer_class = AppointmentSerializer
			permission_classes = [AllowAny]
			doctorId = request.query_params.get('doctorId',None)
			if doctorId is not None:
				doctors = doctors.filter(doctorId__icontains=doctorId)
				
			appointment_serializer = AppointmentSerializer(doctors, Many=True)
			return JsonResponse(appointment_serializer.data, safe=False)
			
		elif request.method == 'POST':
			doctor_data = JSONParser().parse(request)
			appointment_serializer = AppointmentSerializer(data=doctor_data)
			if appointment_serializer.is_valid():
				appointment_serializer.save()
				return JsonResponse(appointment_serializer.data, status=status.HTTP_201_CREATED)
			return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			
	def get_serializer_class(self):
		if self.request.method in ('GET','POST'):
			return AppointmentSerializer
		return self.serializer_class
'''
	
