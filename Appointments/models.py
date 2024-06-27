from django.db import models

from Patients.models import Patient
from Receptionists.models import Receptionist
from Doctors.models import Doctor


# Create your models here.
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)