from django.contrib import admin

from .models import CO2_Emission
from .models import SO2_Emission
from .models import NOX_Emission
from .models import HeatRate
from .models import Co2_Reserve

admin.site.register(CO2_Emission)
admin.site.register(SO2_Emission)
admin.site.register(NOX_Emission)
admin.site.register(HeatRate)
admin.site.register(Co2_Reserve)
