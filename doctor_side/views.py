from django.shortcuts import render, get_object_or_404
from Appointments.serializers import AppointmentSerializer
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from Appointments.models import Appointment  # Ensure the Appointment model is imported

@api_view(['GET'])
def index(request):
    return render(request, 'doctor_side/index.html')


@api_view(['GET', 'POST'])
def appointments(request, id):
    if request.method == 'GET':
        try:
            appointments = Appointment.objects.filter(doctor=id)
            if not appointments.exists():
                return Response({"error": "No appointments found for this doctor"}, status=status.HTTP_404_NOT_FOUND)
            return render(request, 'doctor_side/appointments.html', {'appointments': appointments})
        except Appointment.DoesNotExist:
            return Response({"error": "No appointments found for this doctor"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    elif request.method == 'POST':
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
def about_appointment(request, doctor, id):
    try:  
        appointments = Appointment.objects.filter(doctor=doctor, patient=id) 
        if appointments.exists():
            appointments_data = AppointmentSerializer(appointments, many=True).data
            return render(request, 'doctor_side/about-appointment.html', {'appointments': appointments_data}) 
        else:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
