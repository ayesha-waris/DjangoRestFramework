from rest_framework import viewsets

from api.mixin import StaffEditorPErmissionMixin
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(
  StaffEditorPErmissionMixin,
  viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
   