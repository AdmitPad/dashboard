from __future__ import absolute_import

from django.contrib import admin
from .models import Metric, Datum

class MetricAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_dashboard', 'show_sparkline', 'period')
    list_editable = ('show_on_dashboard', 'show_sparkline', 'period')
    prepopulated_fields = {'slug': ['name']}

for MC in Metric.subclasses_for_display():
    admin.site.register(MC, MetricAdmin)

admin.site.register(Datum, 
    list_display = ('timestamp', 'metric', 'measurement'),
)