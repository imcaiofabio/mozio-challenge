from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.service_area import ServiceArea
from app.serializers.service_area import ServiceAreaSerializer


class ServiceAreaAPIView(APIView):
    def get(self, request):
        service_areas = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_areas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_service_area(self, pk):
        try:
            return ServiceArea.objects.get(pk=pk)
        except ServiceArea.DoesNotExist:
            return None

    def get_object_or_404(self, pk):
        service_area = self.get_service_area(pk)
        if service_area is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return service_area

    def get(self, request, pk=None):
        if pk is not None:
            service_area = self.get_object_or_404(pk)
            serializer = ServiceAreaSerializer(service_area)
            return Response(serializer.data)
        else:
            return self.get(request)

    def put(self, request, pk=None):
        if pk is not None:
            service_area = self.get_object_or_404(pk)
            serializer = ServiceAreaSerializer(service_area, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            service_area = self.get_object_or_404(pk)
            service_area.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
