from django.shortcuts import render

from rest_framework import generics
from .models import Advert
from .serializers import AdvertSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

# Для увеличения просмотров
from django.db.models import F

class AdvertListView(generics.ListAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer
    renderer_classes = [JSONRenderer]

class AdvertDetailView(generics.RetrieveAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer
    renderer_classes = [JSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views = F('views') + 1
        instance.save(update_fields=['views'])
        return super().retrieve(request, *args, **kwargs)