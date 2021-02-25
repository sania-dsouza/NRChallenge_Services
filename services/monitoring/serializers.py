from rest_framework import serializers

from .models import CO2_Emission
from .models import SO2_Emission
from .models import NOX_Emission
from .models import HeatRate
from .models import Co2_Reserve


class CO2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CO2_Emission
        fields = ('emission_Mt', 'measured_date', 'measured_at_minute')


class SO2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SO2_Emission
        fields = ('emission_Mt', 'measured_date', 'measured_at_minute')


class NOX_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NOX_Emission
        fields = ('emission_Mt', 'measured_date', 'measured_at_minute')


class HeatRate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = HeatRate
        fields = ('heat_rate', 'measured_date', 'measured_at_minute')


class Co2_Reserve_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Co2_Reserve
        fields = ('co2_store', 'measured_date', 'measured_at_minute')