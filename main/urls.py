from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name=''),

    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),
    
    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    # path('patientsignup', views.patient_signup_view),
]