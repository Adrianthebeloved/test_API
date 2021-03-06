from http.client import NOT_FOUND
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import EmployeeSerializer, EmployerSerializer
from .models import Employee, Employer
import random
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from app1 import serializers

class EmployeeListView(APIView):

    def get(self, request, format=None):
        """Allows the user to get a list of all employees"""
    
        all_data = Employee.objects.all()

        serializer = EmployeeSerializer(all_data, many=True)

        data = {
            'message' : 'success',
            'data_count' : len(all_data),
            'data' : serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method='post', request_body=EmployeeSerializer())
    @action(methods=['post'], detail=True)
    def post(self, request, format=None):
        """API View to create new employees"""

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["employee_num"] = "".join([str(random.choice(range(10))) for _ in range(6)])
            serializer.save()

            data = {
                'message':'success',
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            data = {
                'message':'failed',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):

    def get_object(self, employee_id):
        try:
            return Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise NotFound(detail={'message': 'Employee not found'}, code=status.HTTP_404_NOT_FOUND)

    def get(self, request, employee_id, format=None):
        """Api view to get details of an employee"""
        obj = self.get_object(employee_id)
        serializer = EmployeeSerializer(obj)

        data = {
            'message' : 'success',
            'data' : serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method='put', request_body=EmployeeSerializer())
    @action(methods=['put'], detail=True)
    def put(self, request, employee_id, format=None):
        """API View to edit employees"""

        obj = self.get_object(employee_id)
        serializer = EmployeeSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            if 'employee_num' in serializer.validated_data.keys():
                raise PermissionDenied(detail={'message':'You cannot edit your employee number'}, code=status.HTTP_403_FORBIDDEN)
            serializer.save()

            data = {
                'message':'success',
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)

        else:
            data = {
                'message':'failed',
                'error':serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id, format=None):
        """Delete an employee"""

        obj = self.get_object(employee_id)
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)




class EmployerListView(APIView):

    def get(self, request, format=None):
        """Allows the user to get a list of all employers"""

        all_data = Employer.objects.all()

        serializer = EmployerSerializer(all_data, many=True)

        data = {
            'message' : 'success',
            'data_count' : len(all_data),
            'data' : serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method='post', request_body=EmployerSerializer())
    @action(methods=['post'], detail=True)
    def post(self, request, format=None):
        """API View to create new employers"""
        serializer = EmployerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["company_num"] = "".join([str(random.choice(range(10))) for _ in range(6)])
            serializer.save()

            data = {
                'message':'success',
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            data = {
                'message':'failed',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class EmployerDetailView(APIView):

    def get_object(self, employer_id):
        try:
            return Employer.objects.get(id=employer_id)
        except Employer.DoesNotExist:
            raise NotFound(detail={'message': 'Employer not found'}, code=status.HTTP_404_NOT_FOUND)

    def get(self, request, employer_id, format=None):
        """Api view to get details of an employer"""
        obj = self.get_object(employer_id)
        serializer = EmployerSerializer(obj)

        data = {
            'message' : 'success',
            'data' : serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method='put', request_body=EmployerSerializer())
    @action(methods=['put'], detail=True)
    def put(self, request, employer_id, format=None):
        """API View to edit employers"""

        obj = self.get_object(employer_id)
        serializer = EmployerSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            if 'employer_num' in serializer.validated_data.keys():
                raise PermissionDenied(detail={'message':'You cannot edit your employer number'}, code=status.HTTP_403_FORBIDDEN)
            serializer.save()

            data = {
                'message':'success',
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)

        else:
            data = {
                'message':'failed',
                'error':serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employer_id, format=None):
        """Delete an employer"""

        obj = self.get_object(employer_id)
        obj.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
