from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(models.Offer, OfferAdmin)
admin.site.register(models.Product, ProductAdmin)