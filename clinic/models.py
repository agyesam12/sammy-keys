from django.db import models
from django.contrib.auth.models import AbstractUser


#Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=40, null=True, blank=False)
    specialization = models.CharField(max_length=60,null=True,blank=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='doctor')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name + "--" +  self.user.name
