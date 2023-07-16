from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models.provider import Provider
from app.serializers.provider import ProviderSerializer


class ProviderAPIView(APIView):
    def get(self, request):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_provider(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return None

    def get_object_or_404(self, pk):
        provider = self.get_provider(pk)
        if provider is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return provider

    def get(self, request, pk=None):
        if pk is not None:
            provider = self.get_object_or_404(pk)
            serializer = ProviderSerializer(provider)
            return Response(serializer.data)
        else:
            return self.get(request)

    def put(self, request, pk=None):
        if pk is not None:
            provider = self.get_object_or_404(pk)
            serializer = ProviderSerializer(provider, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            provider = self.get_object_or_404(pk)
            provider.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

