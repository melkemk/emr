from django.db import models

from Patients.models import Patient

# Create your models here.
class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    generated_date = models.DateTimeField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)