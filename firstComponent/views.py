from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# importaciones de modelos agregados
from firstComponent.models import FristModel

# importaciones de serializadores
from firstComponent.serializers import firstComponentSerializer

# Create your views here.
class PrimerTablaList(APIView):
    def get(request, format=None):
        querySet=FristModel.objects.all()
        serializer=firstComponentSerializer(querySet,many=True ,context={'request':request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=firstComponentSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "data":serializer.data, "status":status.HTTP_201_CREATED})
        else:
            return Response({"success":False, "data":serializer.errors, "status":status.HTTP_400_BAD_REQUEST})
    
class FirstView(APIView):

    def get_FirstComponent(self, pk):
        try:
            return FristModel.objects.get(pk=pk)
        except FristModel.DoesNotExist:
            return 404
    
    def get(self, request, pk, format=None):
        firstComponent = self.get_FirstComponent(pk)
        if firstComponent != 404:
            serializer = firstComponentSerializer(firstComponent, context={'request':request})
            return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})
        else:
            return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})
    
    def put(self, request, pk, format=None):
        firstComponent = self.get_FirstComponent(pk)
        if firstComponent != 404:
            serializer = firstComponentSerializer(firstComponent, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})
            else:
                return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})
        else:
             return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})
             
    def delete(self, request, pk, format=None):
        firstComponent = self.get_FirstComponent(pk)
        if firstComponent != 404:
            serializer = firstComponentSerializer(id, context={'request':request})
            firstComponent.delete()
            return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})
        else:
            return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})

    