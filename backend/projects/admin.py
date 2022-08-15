from django.contrib import admin


from .models import Product
from .serializers import ProductSerializer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display = ("title", "content","price")



admin.site.register(Product, ProductAdmin)