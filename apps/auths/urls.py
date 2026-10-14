from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthsViewset

router = DefaultRouter()
router.register(r"", AuthsViewset, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
]
