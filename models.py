from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Sensor(models.Model):
    Sensor_name = models.CharField(max_length=12, null=True)
    owner = models.ForeignKey(User)

class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor)
    reading = models.IntegerField(max_length=4)
    reading_time = models.DateTimeField()



