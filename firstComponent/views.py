from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# importaciones de modelos agregados
from firstComponent.models import FristModel

# importaciones de serializadores
from firstComponent.serializers import FirstComponentSerializer

# Create your views here.
class PrimerTablaList(APIView):
    def get(self, format=None):
        queryset=FristModel.objects.all()
        serializer=FirstComponentSerializer(queryset,many=True ,context={'request':self})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=FirstComponentSerializer(data=request.data, context={'request':request})
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
        first_component = self.get_FirstComponent(pk)
        if first_component != 404:
            serializer = FirstComponentSerializer(first_component, context={'request':request})
            return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})
        else:
            return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})
    
    def put(self, request, pk, format=None):
        first_component = self.get_FirstComponent(pk)
        if first_component != 404:
            serializer = FirstComponentSerializer(first_component, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})
            else:
                return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})
        else:
             return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})
             
    def delete(self, request, pk, format=None):
        first_component = self.get_FirstComponent(pk)
        if first_component != 404:
            serializer = FirstComponentSerializer(id, context={'request':request})
            first_component.delete()
            return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})
        else:
            return Response({"success":False, "data":NULL, "status":status.HTTP_400_BAD_REQUEST})

    