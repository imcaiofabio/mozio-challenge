from django.db import models
from app.models.provider import Provider
from app.models.service_area import ServiceArea


class Polygon(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    service_area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)
    geometry = models.JSONField()
