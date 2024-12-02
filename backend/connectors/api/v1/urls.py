from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137647ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137647", Testconnectors137647ViewSet, basename="testconnectors137647"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
