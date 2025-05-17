from django.contrib import admin
from .models import Advert, Category, City

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'views')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass