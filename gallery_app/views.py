from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView , UpdateView , DeleteView, CreateView
from .models import Gallery
from .forms import GalleryForm

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
    
class GalleryDelete(View):
    def get(self, request, id):
        gallery = get_object_or_404(Gallery, pk=id)
        gallery.delete()
        return redirect(reverse_lazy('gallery_list'))

class Gallery_create(CreateView):
    model = Gallery
    template_name = "gallery/gallery_Create.html"
    
    form_class = GalleryForm
    success_url = reverse_lazy('gallery_list')

