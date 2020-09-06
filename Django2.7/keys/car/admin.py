from django.contrib import admin

# Register your models here.
from . models import Car


admin.site.register(Car)

# car_1 = Car.objects.first()
# cfe = car_1.first_owner
# User =  cfe.__class__
# first_user = User.objects.first()