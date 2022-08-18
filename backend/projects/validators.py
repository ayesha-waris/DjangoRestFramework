from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs:
        raise serializers.ValidationError("Title already exists")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
