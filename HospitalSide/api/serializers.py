from rest_framework import serializers
from HospitalSide.models import Appointment, Doctor, Patient
from django.contrib.auth.models import User
	   
class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = '_all_'


class DoctorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class PatientListSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	
	class Meta:
		model = Patient
		fields = '__all__'

class PatientCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = '__all__'
