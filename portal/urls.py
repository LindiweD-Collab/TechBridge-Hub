
from django.urls import path
from . import views 

urlpatterns = [
   
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/signup/', views.signup, name='signup'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]