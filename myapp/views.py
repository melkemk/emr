from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def login_view(request):
    return render(request, 'login.html')

def admin_side_view(request):
    return render(request, 'doctor_side/about-appointment.html')  # Adjust the path as needed
