from rest_framework import serializers
from app.models.service_area import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'price', 'geojson']
