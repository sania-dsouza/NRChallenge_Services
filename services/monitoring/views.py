from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CO2_Emission
from .models import SO2_Emission
from .models import NOX_Emission

from .serializers import CO2_Serializer
from .serializers import SO2_Serializer
from .serializers import NOX_Serializer


# CO2 Emissions
@api_view(['GET'])
def co2_emissions(request):
    snippets = CO2_Emission.objects.all()
    serializer = CO2_Serializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def co2_emissions_by_ts(request, date, minute):
    snippet = CO2_Emission.objects.get(measured_date=date, measured_at_minute=minute);
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
def so2_emissions_by_ts(request, date, minute):
    snippet = SO2_Emission.objects.get(measured_date=date, measured_at_minute=minute);
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
def nox_emissions_by_ts(request, date, minute):
    snippet = NOX_Emission.objects.get(measured_date=date, measured_at_minute=minute);
    serializer = NOX_Serializer(snippet)
    # print(snippet.local_currency)
    return Response(serializer.data)
