from django.shortcuts import render
from django.views.generic import ListView
from .models import Gallery

class Gallery_list(ListView):
    model = Gallery
    template_name = "gallery/gallery_list.html"
    context_object_name = "galleries"


