from django.contrib import admin
from .models import Sensor, SensorReading

admin.site.register(Sensor)
admin.site.register(SensorReading)
