from rest_framework import serializers
from .models import  LabTechnician,LabTest

class LabTechniciansSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LabTechnician
        fields = '__all__'
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LabTest
        fields = '__all__'