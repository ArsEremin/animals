from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    login = models.CharField(verbose_name='Id', db_index = True, unique = True, max_length=32)
    firstname = models.CharField(verbose_name='Firtsname', max_length=64)
    lastname = models.CharField(verbose_name='Lastname', max_length=64)
    year = models.IntegerField(verbose_name='Year',  max_length=4)
    phonenumber = models.CharField(verbose_name='Phone number', unique = True, max_length=15)
    authtoken_token = models.CharField(max_length = 1900)
