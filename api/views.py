from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status

class studentApi(APIView):
    def get(self, request, pk=None, format=None):
      id = pk 
      if id is not None:
          stu = Student.objects.get(pk=id)
          serializer = StudentSerializer(stu)
          return Response(serializer.data)
      stu = Student.objects.all()
      serializer = StudentSerializer(stu, many = True)
      return Response(serializer.data)
    
    def post(self,request, format=True):
      if request.method == 'POST':
        serializer = StudentSerializer( data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Created'} , status=status.HTTP_201_CREATED ) # Created
      return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request, pk, format=True):
      if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    def delete(self,request, pk, format=True):
      if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})