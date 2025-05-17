from django import forms
from .models import Gallery
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from users.models import CustomUser
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'cover_image', 'description']



class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser  # Use your custom user model here
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['role']
        if commit:
            user.save()
        return user