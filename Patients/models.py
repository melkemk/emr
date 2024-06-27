from django.db import models

from Doctors.models import Doctor

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    employer = models.CharField(max_length=100, blank=True, null=True)
    insurance_info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Inpatient(models.Model):
    inpatient_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    admission_date = models.DateTimeField()
    room_number = models.IntegerField()
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2)
    discharge_date = models.DateTimeField(blank=True, null=True)
    discharge_summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


