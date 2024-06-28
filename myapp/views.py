from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.shortcuts import render
from Doctors.models import Doctor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import bcrypt
@api_view(['POST',"GET"])
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        try:
            doctor = Doctor.objects.get(email=email)
            
            if bcrypt.checkpw(password.encode('utf-8'), doctor.password.encode('utf-8')):
                request.session['doctor_id'] = doctor.doctor_id 
                return  redirect('/doctor_side/appointments/')

            else:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
    
    return render(request, 'login.html')

def admin_side_view(request):
    return render(request, 'doctor_side/about-appointment.html')  # Adjust the path as needed
