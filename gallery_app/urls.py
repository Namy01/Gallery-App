from django.urls import path
from .views import Gallery_list

urlpatterns = [
    path('', Gallery_list.as_view(), name='gallery_list'),
]