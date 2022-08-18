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
        if (instance):
            # data = model_to_dict(instance)
            data = ProductSerializer(instance).data
        return Response(data)

    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            # instance = serializer.save()

            instance = serializer.data
            print(instance)
        return Response(instance)
