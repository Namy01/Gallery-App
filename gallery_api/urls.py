from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryViewSet

router = DefaultRouter()
router.register(r'galleries', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
