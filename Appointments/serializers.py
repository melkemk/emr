from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['appointment_id', 'patient_id', 'appointment_date', 'status', 'patient_name']

    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"
