from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CO2_Emission
from .models import SO2_Emission
from .models import NOX_Emission

from .serializers import CO2_Serializer
from .serializers import SO2_Serializer
from .serializers import NOX_Serializer

import random, time


# Generate random CO2, SO2, NOX emission values , one each minute
def create_random_emissions(request):
    for i in range(1440):
        rand_float_CO2 = random.random() * 100
        rand_float_SO2 = random.random() * 10
        rand_float_NOX = random.random() * 20
        CO2_Emission.objects.get_or_create(emission_Mt=rand_float_CO2, measured_at_minute=i)
        SO2_Emission.objects.get_or_create(emission_Mt=rand_float_SO2, measured_at_minute=i)
        NOX_Emission.objects.get_or_create(emission_Mt=rand_float_NOX, measured_at_minute=i)
        time.sleep(60.0)    # sleep for 1 minute
    return render(request, 'monitoring/start_plant.html', {})


# CO2 Emissions
@api_view(['GET'])
def co2_emissions(request):
    snippets = CO2_Emission.objects.all()
    serializer = CO2_Serializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def co2_emissions_by_ts(request, measured_date, measured_at_minute):
    snippet = CO2_Emission.objects.get(measured_date=measured_date, measured_at_minute=measured_at_minute);
    serializer = CO2_Serializer(snippet)
    # print(snippet.local_currency)
    return Response(serializer.data)


# SO2 Emissions
@api_view(['GET'])
def so2_emissions(request):
    snippets = SO2_Emission.objects.all()
    serializer = SO2_Serializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def so2_emissions_by_ts(request, measured_date, measured_at_minute):
    snippet = SO2_Emission.objects.get(measured_date=measured_date, measured_at_minute=measured_at_minute);
    serializer = SO2_Serializer(snippet)
    # print(snippet.local_currency)
    return Response(serializer.data)


# NOX Emissions
@api_view(['GET'])
def nox_emissions(request):
    snippets = NOX_Emission.objects.all()
    serializer = NOX_Serializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def nox_emissions_by_ts(request, measured_date, measured_at_minute):
    snippet = NOX_Emission.objects.get(measured_date=measured_date, measured_at_minute=measured_at_minute);
    serializer = NOX_Serializer(snippet)
    # print(snippet.local_currency)
    return Response(serializer.data)
