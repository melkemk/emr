from rest_framework import serializers # type: ignore
from .models import Inpatient,Patient 

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Patient
        fields = '__all__'
class InpatientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Inpatient
        fields = '__all__'