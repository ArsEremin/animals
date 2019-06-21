from django.shortcuts import render
from Students.serializers import StudentDetailSerializer,StudentListSerializer
from rest_framework import generics
from Students.models import Student

class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentDetailSerializer

class StudentListView(generics.ListAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()