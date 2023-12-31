from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.service_area import ServiceArea
from app.serializers.service_area import ServiceAreaSerializer
from drf_yasg.utils import swagger_auto_schema


class ServiceAreaAPIView(APIView):
    def get_service_area(self, pk):
        try:
            return ServiceArea.objects.get(pk=pk)
        except ServiceArea.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk:
            service_area = self.get_service_area(pk)

            if service_area:
                serializer = ServiceAreaSerializer(service_area)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            service_areas = ServiceArea.objects.all()
            serializer = ServiceAreaSerializer(service_areas, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(request_body=ServiceAreaSerializer)
    def post(self, request):
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ServiceAreaSerializer)
    def put(self, request, pk):
        if pk:
            service_area = self.get_service_area(pk)

            if service_area:
                serializer = ServiceAreaSerializer(service_area, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if pk:
            service_area = self.get_service_area(pk)

            if service_area:
                service_area.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
