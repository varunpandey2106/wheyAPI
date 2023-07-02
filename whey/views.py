from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Whey
from .serializer import WheySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def whey_list(request, format=None):
    if request.method== 'GET':
        whey=Whey.objects.all() #get all the wheys
        serializer=WheySerializer(whey,many=True ) #serialize them
        return Response(serializer.data)
    
    if request.method== 'POST':
        serializer=WheySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE', ])
def whey_detail(request, id, format=None):
    
    try:
        whey = Whey.objects.get(pk=id)
    except Whey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=WheySerializer(whey)#from try and exception, avoiding repititon
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer=WheySerializer(whey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        whey.delete()
        return Response(status.HTTP_204_NO_CONTENT)

