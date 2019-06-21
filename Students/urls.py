from django.contrib import admin
from django.urls import include, path
from Students.views import *

urlpatterns = [
    path('create/', StudentCreateView.as_view()),
    path('', StudentListView.as_view()),
    path('<int:pk>/',StudentDetailView.as_view())
]