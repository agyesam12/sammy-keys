from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


#Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
    

class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    number = models.CharField(max_length=200, null=True, blank=False)
    specialization = models.CharField(max_length=50, null=True, blank=False)


    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    address = models.CharField(max_length=300, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=False)


    def __str__(self):
        return self.name



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()


    def __str__(self):
        return self.doctor.name + "--" +  self.patient.name



