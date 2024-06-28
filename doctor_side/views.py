from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Appointments.models import Appointment  # Ensure the Appointment model is imported

@api_view(['GET'])
def index(request):
    return render(request, 'doctor_side/index.html')

@api_view(['GET', 'POST'])
def appointments(request):
    if request.method == 'GET':
        # Fetch all appointments
        appointments = Appointment.objects.all()
        return render(request, 'doctor_side/appointments.html', {'appointments': appointments})
    elif request.method == 'POST':
        # Handle creation of a new appointment
        # You need to define AppointmentSerializer in your serializers.py
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def edit_appointment(request):
    if request.method == 'PUT':
        # Handle the editing of an existing appointment
        appointment_id = request.data.get('appointment_id')
        appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def about_appointment(request, appointment_id=None):
    if appointment_id is not None:
        appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
        return render(request, 'doctor_side/about_appointment.html', {'appointment': appointment})
    return Response({'error': 'ID is required to view appointment details'}, status=status.HTTP_400_BAD_REQUEST)
