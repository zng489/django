from django.contrib import admin

# Register your models here.
from .models import Product, BlogPost, DataRecord


admin.site.register(Product)