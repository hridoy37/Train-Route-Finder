from rest_framework import serializers
from .models import Train, Station, TrainRoute

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class TrainRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainRoute
        fields = '__all__'
