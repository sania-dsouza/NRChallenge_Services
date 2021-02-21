from rest_framework import serializers

from .models import CO2_Emission
from .models import SO2_Emission
from .models import NOX_Emission


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
