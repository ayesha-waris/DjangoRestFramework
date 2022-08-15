import json
from django.forms.models import model_to_dict
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from projects.models import Product
from projects.serializers import ProductSerializer


class api_home(APIView):
    def get(self, request):
        instance = Product.objects.get(pk=1)
        print(instance)
        data = {}
        if(instance):
    # data = model_to_dict(instance)
            data = ProductSerializer(instance).data
        return Response(data)