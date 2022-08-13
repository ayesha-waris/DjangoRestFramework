import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):

  body = request.body 
  print(body)
  # print(request.GET)
  # print(dict(request.headers))
  data = {}
  try:
    data = json.loads(body)
  except:
    pass
  # print(data)
  data['param'] = dict(request.GET)
  data['headers'] = dict(request.headers)
  data['content_type'] = request.content_type
  return JsonResponse(data
  )