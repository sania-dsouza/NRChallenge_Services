from django.contrib import admin

from .models import CO2_Emission
from .models import SO2_Emission
from .models import NOX_Emission

admin.site.register(CO2_Emission)
admin.site.register(SO2_Emission)
admin.site.register(NOX_Emission)

