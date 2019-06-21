from rest_framework import serializers
from Students.models import Student

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('login','firstname','lastname')


