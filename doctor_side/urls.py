from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  
    path('appointments', appointments, name = 'appointments'),
    path('edit_appointment', edit_appointment, name = 'edit-appointment'),
    path('about-appointment/<int:appointment_id>/', about_appointment, name='about-appointment'),

]
 