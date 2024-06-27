from django.db import models

from Patients.models import Inpatient, Patient

# Create your models here.
class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    inpatient = models.ForeignKey(Inpatient, on_delete=models.CASCADE)
    services = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    billing_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)