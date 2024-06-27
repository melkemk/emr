from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='default@example.com')

    specialization = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100) 

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
