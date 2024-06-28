from django.urls import path
from .views import  *
 
urlpatterns = [
    path('login/', login_view, name='login'),
    path('admin/', admin_side_view, name='admin_side'),
] 
