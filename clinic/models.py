from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


#Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
    


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='doctor')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.user.username
