from django.contrib import admin

# Register your models here.
from .models import Product

"""every app needs to be registered at the admin"""
admin.site.register(Product)
