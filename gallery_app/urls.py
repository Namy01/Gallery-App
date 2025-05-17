from django.urls import path
from .views import Gallery_list, Gallery_edit, Gallery_create, GalleryDelete, RegisterView, CustomLoginView, HomeView

urlpatterns = [
    path('gallery_lists', Gallery_list.as_view(), name='gallery_lists'),
    path('edit-gallery/<int:id>/', Gallery_edit.as_view(), name='edit-gallery'),
    path('create-gallery', Gallery_create.as_view(), name='create-gallery'),
    path('del/<int:id>/', GalleryDelete.as_view(), name='del'),
    path('register', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='gallery_list'),
]