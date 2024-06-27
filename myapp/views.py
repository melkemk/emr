from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def admin_side_view(request):
    return render(request, 'doctor_side/about-appointment.html')  # Adjust the path as needed

# Create similar views for other sections
