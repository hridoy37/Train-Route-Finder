from django.contrib import admin
from .models import Train, Station, TrainRoute

class TrainAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TrainRouteAdmin(admin.ModelAdmin):
    list_display = ('train', 'from_station', 'to_station', 'departure_time', 'arrival_time', 'fare')
    list_filter = ('train', 'from_station', 'to_station')
    search_fields = ('train__name', 'from_station__name', 'to_station__name')

# Register your models here.
admin.site.register(Train, TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(TrainRoute, TrainRouteAdmin)
