from wsgiref.validate import validator
from requests import request
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]



    def create(self, validated_data):
        email = validated_data.pop('email')
        return Product.objects.create(**validated_data)
      #  obj = super().create(validated_data)
      #  return obj

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
      # return f'/api/v2/products/{obj.pk}/'
        request = self.context.get('request')
        if reverse is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
