from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL
# Create your models here.
"""
Forengin Keys
"""
# class Car(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name
    
    
    
    
    
# class Car(models.Model):
#     drivers = models.ManyToManyField(User )
#     name = models.CharField(max_length=200)
    
    # def __str__(self):
    #     return self.name
    
""" 
    car1 = Car.objects.first()
    user_qs = car1.drivers.all()
    
    cfe = user_qs.first()
    cfe.car_set.all()
    
    Car.objects.filter(drivers=cfe)
    Car.objects.filter(drivers_in=user_qs)
    
"""
    
    

    
class Car(models.Model):
    first_owner = models.OneToOneField(User,on_delete=models.CASCADE )
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
