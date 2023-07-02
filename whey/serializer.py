from rest_framework import serializers
from .models import Whey

class WheySerializer(serializers.ModelSerializer):
    class Meta:
        model= Whey
        fields=['id', 'name', 'brand_name', 'protein_content_in_g']
