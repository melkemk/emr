from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.shortcuts import render
from Patients.models import Patient
from Patients.serializers import PatientSerializer
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def add_patient(request):  
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response({"asdf":"asdf"})
    return render(request, 'receptioinst_side/add-patient.html')

@api_view(['GET', 'POST'])
def edit_patient(request):
    if request.method == 'POST': 
        try:
            id = request.data.get('doctor_id') 
            if not id :
                return Response({'error': 'id  is required'}, status=status.HTTP_400_BAD_REQUEST)
            patient  = Patient.objects.get(patient_id=id ) 
        except Patient.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
 
        serializer = PatientSerializer(patient, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return render(request, 'receptioinst_side/edit-patient.html')
@api_view(['GET'])
def about_patient(request, patient_id =None):
    if id is not None:
        patient  = get_object_or_404(Patient , patient_id=patient_id )
    return render(request, 'receptioinst_side/about-patient.html',{'doctor': patient}) 
    return Response({'error': 'ID is required to view doctor details'}, status=status.HTTP_400_BAD_REQUEST)
