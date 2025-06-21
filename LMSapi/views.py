from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Teacher, Student
from LMSapi.serializers import TeacherSerializer, StudentSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TeacherApiView(APIView):
    def get_object_instance(self, pk):
        try:
            return Teacher.objects.get(pk = pk)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get (self, request, pk ) :
        teacher= self.get_object_instance(pk)
        serializers= TeacherSerializer(teacher)
        return Response (serializers.data) 
    
    def put (self, request, pk):
        teacher= self.get_object_instance(pk)
        serializers= TeacherSerializer(teacher,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data)
        return Response(serializers.eroors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        teacher= self.get_object_instance(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeacherApiListCreateView(APIView):
    def get(self, request):
        teachers= Teacher.objects.all()
        serializers= TeacherSerializer(teachers, many= True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        teacher_data= request.data()
        serializers= TeacherSerializer(data= teacher_data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    