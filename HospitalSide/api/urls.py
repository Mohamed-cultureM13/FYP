from django.urls import path,include
#from .import views
from rest_framework import routers
from HospitalSide.api.views import PatientAPIView , DoctorAPIView #, AppointmentAPIView

#router = routers.DefaultRouter(trailing_slash=False)
#router.register('Patient',views.patient_book_appointment_view)

urlpatterns = [
#path('',include(router.urls)),
path('patient/',PatientAPIView.as_view(),name = 'patient-callbackurl'),
path('doctor/',DoctorAPIView.as_view(),name = 'doctor-selection'),
#path('appointment/',AppointmentAPIView.as_view(),name = 'appointment-validation'),
]
