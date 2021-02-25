import datetime

from django.db import models
from time import time


class CO2_Emission(models.Model):
    emission_Mt = models.FloatField()       # emissions in Metric tonnes
    measured_date = models.DateField()
    measured_at_minute = models.PositiveSmallIntegerField(default=1)   # Minute of the emission

    def __str__(self):
        return str(self.emission_Mt) + " metric tonnes of CO2 measured on " + str(self.measured_date) + " at minute " + str(self.measured_at_minute)


class SO2_Emission(models.Model):
    emission_Mt = models.FloatField()       # emissions in Metric tonnes
    measured_date = models.DateField()
    measured_at_minute = models.PositiveSmallIntegerField(default=1)  # Minute of the emission

    def __str__(self):
        return str(self.emission_Mt) + " metric tonnes of SO2 measured on " + str(self.measured_date) + " at minute " + str(self.measured_at_minute)


class NOX_Emission(models.Model):
    emission_Mt = models.FloatField()       # emissions in Metric tonnes
    measured_date = models.DateField()
    measured_at_minute = models.PositiveSmallIntegerField(default=1)  # Minute of the emission

    def __str__(self):
        return str(self.emission_Mt) + " metric tonnes of NOX measured on " + str(self.measured_date) + " at minute " + str(self.measured_at_minute)


class HeatRate(models.Model):
    heat_rate = models.IntegerField()
    measured_date = models.DateField()
    measured_at_minute = models.PositiveSmallIntegerField(default=1)  # Minute of the emission

    def __str__(self):
        return str(self.heat_rate)


class Co2_Reserve(models.Model):
    co2_store = models.PositiveBigIntegerField()
    measured_date = models.DateField()
    measured_at_minute = models.PositiveSmallIntegerField(default=1)  # Minute of the reserve measurement

    def __str__(self):
        return str(self.co2_store) + " measured at " + str(self.measured_date) + " at minute " + str(self.measured_at_minute)

