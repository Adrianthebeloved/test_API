from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee, name='employee_list'),
    path('employers/', views.employer, name='employer_list'),
]