from django.urls import path
from app.views.provider import ProviderAPIView
from app.views.service_area import ServiceAreaAPIView

urlpatterns = [
    path('providers/', ProviderAPIView.as_view(), name='provider-list'),
    path('providers/<int:pk>/', ProviderAPIView.as_view(), name='provider-detail'),
    path('service-areas/', ServiceAreaAPIView.as_view(), name='service-area-list'),
    path('service-areas/<int:pk>/', ServiceAreaAPIView.as_view(), name='service-area-detail'),
]