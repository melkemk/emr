from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  
    path('about-lab-technician/<int:technician_id>/', about_lab_technician, name='about-lab-technician'), #
    path('about-receptionist/<int:receptionist_id>/', about_receptionist, name='about-receptionist'), #
    path('about-doctor/<int:doctor_id>/', about_doctor, name='about-doctor'),#
    path('add-doctor/', add_doctor, name='add-doctor'), #
    
    path('edit-doctor/', edit_doctor, name='edit-doctor'), #
    path('add-lab-technician/', add_lab_technician, name='add-lab-technician'), #
    path('edit-lab-technician/', edit_lab_technician, name='edit-lab-technician'),
    path('add-receptionist/', add_receptionist, name='add-receptionist'), # 
    path('edit-receptionist/', edit_receptionist, name='edit-receptionist'), #
    path('doctors/', doctors, name='doctors'), 
    path('lab-technicians/', lab_technicians, name='lab-technicians'),
    path('receptionists/', receptionists, name='receptionists'),
    path ('delete-doctor/<int:id>/', delete_doctor,name= 'delete-doctor' ),
    path ('delete-receptionist/<int:id>/', delete_receptionist,name= 'delete-doctor' ),
    path ('delete-technician/<int:id>/', delete_technician,name= 'delete-doctor' ),
]
 