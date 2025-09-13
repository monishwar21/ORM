from django.db import models
from django.contrib import admin

class Cars_DB(models.Model):
      car_name=models.CharField(max_length=30)
      regno=models.IntegerField(primary_key=True)
      carowner_email=models.EmailField()
      carmanufacture_date=models.DateField()
      car_mileage=models.FloatField()

class Cars_DBAdmin(admin.ModelAdmin):
      List_display=["car_name","regno","carowner_email","carmanufacture_date","car_mileage"]


