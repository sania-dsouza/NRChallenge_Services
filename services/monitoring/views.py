
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CO2_Emission, Co2_Reserve
from .models import SO2_Emission
from .models import NOX_Emission
from .models import HeatRate

from .serializers import CO2_Serializer, Co2_Reserve_Serializer
from .serializers import SO2_Serializer
from .serializers import NOX_Serializer
from .serializers import HeatRate_Serializer

import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
application = newrelic.agent.register_application(timeout=10.0)

import random, time
import datetime

# Generate random CO2, SO2, NOX emission values and heat rates, one each minute, also
# get the co2 reserve
def create_random_emissions(request):
    co2_reserve = 1000000   # 1m Mt initially
    for i in range(1, 1441):
        rand_float_CO2 = round(random.random() * 100, 3)
        rand_float_SO2 = round(random.random() * 10, 3)
        rand_float_NOX = round(random.random() * 20, 3)
        rand_int_HR = random.random() *10000
        rand_int_CO2_reserve = random.random() * 15  # assume 15% of all the emissions is sent to the reserve
        CO2_Emission.objects.get_or_create(emission_Mt=rand_float_CO2, measured_date=datetime.datetime.now().date(), measured_at_minute=i)
        SO2_Emission.objects.get_or_create(emission_Mt=rand_float_SO2, measured_date=datetime.datetime.now().date(), measured_at_minute=i)
        NOX_Emission.objects.get_or_create(emission_Mt=rand_float_NOX, measured_date=datetime.datetime.now().date(), measured_at_minute=i)
        HeatRate.objects.get_or_create(heat_rate=rand_int_HR, measured_date=datetime.datetime.now().date(), measured_at_minute=i)
        co2_reserve = co2_reserve + rand_int_CO2_reserve
        Co2_Reserve.objects.get_or_create(co2_store=co2_reserve, measured_date=datetime.datetime.now().date(), measured_at_minute=i)

        # send custom metrics to New Relic
        newrelic.agent.record_custom_metric('Custom/CO2Reading', rand_float_CO2, application)
        newrelic.agent.record_custom_metric('Custom/SO2Reading', rand_float_SO2, application)
        newrelic.agent.record_custom_metric('Custom/NOXReading', rand_float_NOX, application)
        newrelic.agent.record_custom_metric('Custom/HeatRate', rand_int_HR, application)
        newrelic.agent.record_custom_metric('Custom/CO2Reserve', co2_reserve, application)

        time.sleep(60.0)    # sleep for 1 minute
    return render(request, 'monitoring/start_plant.html', {})


# CO2 Emissions: all and emissions by timestamp
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


# SO2 Emissions: all and emissions by timestamp
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


# NOX Emissions: all and emissions by timestamp
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


@api_view(['GET'])
def heat_rate_by_ts(request, measured_date, measured_at_minute):
    snippet = HeatRate.objects.get(measured_date=measured_date, measured_at_minute=measured_at_minute);
    serializer = HeatRate_Serializer(snippet)
    # print(snippet.local_currency)
    return Response(serializer.data)


@api_view(['GET'])
def co2_reserve_by_ts(request, measured_date, measured_at_minute):
    snippet = Co2_Reserve.objects.get(measured_date=measured_date, measured_at_minute=measured_at_minute);
    serializer = Co2_Reserve_Serializer(snippet)
    # print(snippet.local_currency)
    return Response(serializer.data)
