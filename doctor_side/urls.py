from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index1'),  
    path('appointments/<int:id>/', appointments, name='appointments'),
    path('edit_appointment', edit_appointment, name = 'edit-appointment'),
    path('about-appointment/<int:id>/', about_appointment, name='about-appointment'),

]
 