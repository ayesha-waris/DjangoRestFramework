from rest_framework import serializers
from rest_framework import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_url(self, obj):
      return f'/api/v2/products/{obj.pk}/'

    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
