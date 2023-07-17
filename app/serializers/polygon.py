from rest_framework import serializers
from app.models.polygon import Polygon


class PolygonSerializer(serializers.ModelSerializer):
    provider_name = serializers.ReadOnlyField(source='provider.name')
    price = serializers.DecimalField(source='service_area.price', max_digits=10, decimal_places=2)

    class Meta:
        model = Polygon
        fields = ['name', 'provider_name', 'price']