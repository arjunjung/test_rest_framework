from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from api.models import ToyModel
from api.serializers import ToySerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        #JSONRenderer converts dicitionary data to JSON
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        print("Hi i am get")
        #queryset of objects
        all_toys_obj = ToyModel.objects.all()
        all_toys_serialized = ToySerializer(all_toys_obj, many=True)
        all_toys_json = JSONResponse(all_toys_serialized.data)
        return all_toys_json

    elif request.method == 'POST':
        print('Hi i am post request:  ',request)
        toy_data = JSONParser().parse(request)
        print('toydata: in list ',toy_data)
        toy_data_serialized = ToySerializer(data=toy_data)
        if toy_data_serialized.is_valid():
            toy_data_serialized.save()
            return JSONResponse(toy_data_serialized.data, status=status.HTTP_201_CREATED)
        return JSONResponse(toy_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def toy_funs(request,pk):
    try:
        toy = ToyModel.objects.get(pk=pk)
    except ToyModel.DoesNotExist:
        return JSONResponse(data=None,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serialized = ToySerializer(toy)
        return JSONResponse(toy_serialized.data)

    elif request.method == 'PUT':
        #JSONParser converts JSON data to dicitionary
        toy_data = JSONParser().parse(request)
        toy_data_serialized = ToySerializer(toy,data=toy_data)
        if toy_data_serialized.is_valid():
            toy_data_serialized.save()
            return JSONResponse(toy_data_serialized.data)
        return JSONResponse(toy_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return JSONResponse(data=None,status=status.HTTP_204_NO_CONTENT)
