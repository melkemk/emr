from django.urls import path
from . import views 
 
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin/', views.admin_side_view, name='admin_side'),
    # Add paths for other views
] 
 