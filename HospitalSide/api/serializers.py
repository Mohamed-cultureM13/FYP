from rest_framework import serializers

from HospitalSide.models import Patient, Doctor #, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
	    model = Patient
	    fields = ('user','address','mobile','symptoms')
	   
'''class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = ('doctorName','doctorId')'''

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = ('department','user')
