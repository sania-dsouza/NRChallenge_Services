from django.urls import path
from .views import create_random_emissions, co2_emissions, co2_emissions_by_ts, so2_emissions, so2_emissions_by_ts, nox_emissions, nox_emissions_by_ts


urlpatterns = [
    path('start/', create_random_emissions, name='plant_home'),
    path('co2/', co2_emissions, name="co2_emissions"),
    path('co2/<measured_date>/<measured_at_minute>', co2_emissions_by_ts, name="co2_emissions_by_ts"),
    path('so2/', so2_emissions, name="so2_emissions"),
    path('so2/<measured_date>/<measured_at_minute>', so2_emissions_by_ts, name="so2_emissions_by_ts"),
    path('nox/', nox_emissions, name="nox_emissions"),
    path('nox/<measured_date>/<measured_at_minute>', nox_emissions_by_ts, name="nox_emissions_by_ts"),
]
