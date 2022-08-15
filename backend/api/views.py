import json
from django.forms.models import model_to_dict
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Product

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):

  model_data = Product.objects.get(pk=1)
  print(model_data)
  data = {}
  if(model_data):
    data = model_to_dict(model_data)
  return Response(data)