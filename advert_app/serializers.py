from rest_framework import serializers
from .models import Advert

class AdvertSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Advert
        fields = ['id', 'created', 'title', 'description', 'city', 'category', 'views']