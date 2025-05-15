from rest_framework import serializers
from gallery_app.models import Gallery # import from gallery app

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
