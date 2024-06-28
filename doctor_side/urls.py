from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  
    path('appointments/', appointments, name='about-appointment'),
    path('edit_appointment', edit_appointment, name = 'edit-appointment'),
    path('about-appointment/<int:doctor>/<int:id>/', about_appointment, name='about-appointment'),

]
 