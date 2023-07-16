from rest_framework import serializers
from app.models.provider import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone_number', 'language', 'currency']