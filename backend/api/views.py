import json
from django.http import JsonResponse

from projects.models import Product

def api_home(request, *args, **kwargs):

  model_data = Product.objects.get(pk=1)
  data = {}
  if(model_data):
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content
    data['price'] = model_data.price
  return JsonResponse(data
  )