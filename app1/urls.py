from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView().as_view(), name='employee_list'),
    path('employees/<int:employee_id>/', views.EmployeeDetailView().as_view(), name='employee_detail'),
    path('employers/', views.EmployerListView().as_view(), name='employer_list'),
    path('employers/<int:employer_id>/', views.EmployerDetailView().as_view(), name='employer_detail'),
]