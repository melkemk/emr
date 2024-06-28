from django.urls import path
from .views import *

urlpatterns = [
    path('add-patient/', add_patient, name='add-patient'),
    path('edit-patient/', edit_patient, name='edit-patient'),
    path('about-patient/<int:patient_id>/', about_patient, name='about-patient'),#

    
]
