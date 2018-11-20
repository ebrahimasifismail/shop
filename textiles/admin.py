from django.contrib import admin
from textiles.models import Product, ProductImage, SubProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(SubProduct)

