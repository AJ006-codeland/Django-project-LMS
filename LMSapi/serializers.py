from rest_framework import serializers
from core.models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields= ['full_name','email', 'department', 'phone_no','join_date']

class StudentSerializer(serializers.ModelSerializer):
    model= Student
    fields= ['full_name','email', 'semedter','phone_no', 'user']
