from django.db import models

class VIN(models.Model):
    version = models.IntegerField()
    equipment_code = models.CharField(max_length=3)
    year_of_issue = models.IntegerField()
    serial_number = models.CharField(max_length=7)
    place_of_production = models.CharField(max_length=2)