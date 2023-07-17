from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.provider import Provider
from app.serializers.provider import ProviderSerializer
from drf_yasg.utils import swagger_auto_schema


class ProviderAPIView(APIView):
    def get_provider(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk:
            provider = self.get_provider(pk)

            if provider:
                serializer = ProviderSerializer(provider)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            providers = Provider.objects.all()
            serializer = ProviderSerializer(providers, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(request_body=ProviderSerializer)
    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProviderSerializer)
    def put(self, request, pk=None):
        if pk:
            provider = self.get_provider(pk)

            if provider:
                serializer = ProviderSerializer(provider, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            provider = self.get_provider(pk)
            if provider:
                provider.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
