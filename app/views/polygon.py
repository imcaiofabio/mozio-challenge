from django.contrib.gis.geos import Point
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.polygon import Polygon
from app.serializers.polygon import PolygonSerializer


class PolygonView(APIView):
    def get(self, request):
        latitude = float(request.GET.get('lat'))
        longitude = float(request.GET.get('lng'))
        point = Point(longitude, latitude, srid=4326)  # Create a Point object with the given coordinates

        polygons = Polygon.objects.filter(geometry__contains=point)  # Filter polygons that contain the given point

        serializer = PolygonSerializer(polygons, many=True)
        return Response(serializer.data)
