from django.urls import path,include
from .import views
from rest_framework import routers
from HospitalSide.api.views import GetDoctorsByDepartment, PatientListView, CreatePatientView

#router = routers.DefaultRouter(trailing_slash=False)
#router.register('Patient',views.patient_book_appointment_view)

urlpatterns = [
	path('doctors/', GetDoctorsByDepartment.as_view()),
	path('patients/', CreatePatientView.as_view()),
	path('patients/list', PatientListView.as_view())
]
