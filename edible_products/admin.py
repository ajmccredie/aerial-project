from django.contrib import admin
from .models import EdibleProduct, ProductWeightPrice

class ProductWeightPriceInline(admin.TabularInline):
    model = ProductWeightPrice
    extra = 1

@admin.register(EdibleProduct)
class EdibleProductAdmin(admin.ModelAdmin):
    inlines = [ProductWeightPriceInline]
    list_display = (
        'flavour', 'plant_based', 'guest_flavour', 
        'list_allergens',
        'quantity', 'weight', 'price'
    )
    list_filter = (
        'plant_based', 'guest_flavour', 
        'gluten', 'crustaceans', 'eggs', 'fish', 'peanuts', 
        'soybeans', 'milk', 'nuts', 'celery', 'mustard', 
        'sesame_seeds', 'sulphur_dioxide_and_sulphites', 
        'lupin', 'molluscs'
    )
    search_fields = ('flavour', 'details', 'ingredients')
    fieldsets = (
        (None, {
            'fields': ('flavour', 'plant_based', 'guest_flavour', 'details', 'ingredients', 'quantity', 'price', 'rating', 'image_url', 'image')
        }),
        ('Allergens', {
            'fields': (
                'gluten', 'crustaceans', 'eggs', 'fish', 'peanuts', 
                'soybeans', 'milk', 'nuts', 'celery', 'mustard', 
                'sesame_seeds', 'sulphur_dioxide_and_sulphites', 
                'lupin', 'molluscs'
            ),
            'description': "Select all allergens present in this product."
        }),
    )