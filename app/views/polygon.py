from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.polygon import Polygon
from app.serializers.polygon import PolygonSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY


class PolygonView(APIView):
    @swagger_auto_schema(manual_parameters=[
        Parameter('lat', IN_QUERY, type='float'),
        Parameter('lng', IN_QUERY, type='float')])
    def get(self, request):
        latitude = float(request.GET.get('lat'))
        longitude = float(request.GET.get('lng'))

        polygons = Polygon.objects.all()
        matching_polygons = []

        for polygon in polygons:
            if self.point_in_polygon(latitude, longitude, polygon):
                matching_polygons.append(polygon)

        serializer = PolygonSerializer(matching_polygons, many=True)
        return Response(serializer.data)

    @staticmethod
    def point_in_polygon(latitude, longitude, polygon):
        x = longitude
        y = latitude

        num_vertices = len(polygon.coordinates)
        inside = False

        for i in range(num_vertices):
            j = i + 1 if i < num_vertices - 1 else 0
            xi = polygon.coordinates[i]['lng']
            yi = polygon.coordinates[i]['lat']
            xj = polygon.coordinates[j]['lng']
            yj = polygon.coordinates[j]['lat']

            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside

        return inside
