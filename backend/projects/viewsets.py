from rest_framework import viewsets
from rest_framework import mixins
from api.mixin import StaffEditorPErmissionMixin
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(
        StaffEditorPErmissionMixin,
        viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        StaffEditorPErmissionMixin,
        viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})