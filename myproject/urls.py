from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', include('myapp.urls')),  # Replace '/' with an empty string for the root path
    path('admin_side/', include('admin_side.urls')),
    path('doctor_side/', include('doctor_side.urls')),
    path('patient/', include('Patients.urls')),
    path('receptionist/', include('Receptionists.urls')),
]
