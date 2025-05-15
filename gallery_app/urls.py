from django.urls import path
from .views import Gallery_list, Gallery_edit

urlpatterns = [
    path('', Gallery_list.as_view(), name='gallery_list'),
    path('edit-gallery/<int:id>/', Gallery_edit.as_view(), name='edit-gallery')

]