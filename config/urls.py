from django.urls import path
from app.views.provider import ProviderAPIView
from app.views.service_area import ServiceAreaAPIView
from app.views.polygon import PolygonView
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mozio Challenge | Back End Developer position",
        default_version='v0.1',
        contact=openapi.Contact(email="caio.fabio91@gmail.com", url="https://linkedin.com/in/caio-fabio", name="Caio Souza"),
    ),
    public=True,
)

router = routers.DefaultRouter()

urlpatterns = [
    path('providers', ProviderAPIView.as_view(), name='provider-list'),
    path('providers/<int:pk>', ProviderAPIView.as_view(), name='provider-detail'),
    path('service-areas', ServiceAreaAPIView.as_view(), name='servicearea-list'),
    path('service-areas/<int:pk>', ServiceAreaAPIView.as_view(), name='servicearea-detail'),
    path('polygon-lookup', PolygonView.as_view(), name='polygon-lookup-list'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs-view/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
