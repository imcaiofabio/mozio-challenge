from django.urls import path
from app.views.provider import ProviderAPIView
from app.views.service_area import ServiceAreaAPIView
from app.views.polygon import PolygonView

urlpatterns = [
    path('providers', ProviderAPIView.as_view()),
    path('providers/<int:pk>', ProviderAPIView.as_view()),
    path('service-areas', ServiceAreaAPIView.as_view()),
    path('service-areas/<int:pk>', ServiceAreaAPIView.as_view()),
    path('lookup', PolygonView.as_view()),
]
