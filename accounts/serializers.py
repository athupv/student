from rest_framework import serializers
from .models import Student, MarkStudent

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'roll_number', 'name', 'date_of_birth']

class MarkStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkStudent
        fields = ['mark']