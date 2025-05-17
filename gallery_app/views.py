from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView , UpdateView , DeleteView, CreateView, FormView, TemplateView
from django.contrib.auth.views import LoginView
from .models import Gallery
from .forms import GalleryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from django.contrib import messages



class GalleryHomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'creator':
            images = Gallery.objects.filter(creator=request.user)
        elif user.user_type in ['viewer', 'admin']:
            images = Gallery.objects.all()
        else:
            images = []
        
        context = {'images': images}
        return render(request, 'gallery/home.html', context)
    
class Gallery_list(ListView):
    model = Gallery
    template_name = "gallery/gallery_list.html"
    context_object_name = "galleries"

class Gallery_edit(UpdateView):
    model = Gallery
    template_name = "gallery/gallery_edit.html"
    fields = ["title", "cover_gallery"]
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
    form_class = GalleryForm
    template_name = "gallery/gallery_Create.html"
    

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set creator here
        return super().form_valid(form)
    
    form_class = GalleryForm
    success_url = reverse_lazy('gallery_list')
    

class RegisterView(FormView):
    template_name = 'gallery/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created! Please log in.')
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'gallery/login.html'

class HomeView(TemplateView):
    template_name = 'gallery/home.html'