from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , UpdateView
from .models import Gallery

class Gallery_list(ListView):
    model = Gallery
    template_name = "gallery/gallery_list.html"
    context_object_name = "galleries"

class Gallery_edit(UpdateView):
    model = Gallery
    template_name = "gallery/gallery_edit.html"
    fields = ["title", "cover_image"]
    success_url = '/'

    def get_object(self, queryset=None):
        return Gallery.objects.get(id=self.kwargs['id'])
