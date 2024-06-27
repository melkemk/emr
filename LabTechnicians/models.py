from django.db import models

from Patients.models import Patient

# Create your models here.

class LabTechnician(models.Model):
    technician_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LabTest(models.Model):
    labtest_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    technician = models.ForeignKey(LabTechnician, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_date = models.DateTimeField()
    test_result = models.TextField()
    authorized_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
