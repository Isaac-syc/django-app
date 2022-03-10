from asyncio.windows_events import NULL
from tkinter import FALSE
from django.shortcuts import render

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from loadimage.serializers import LoadImageSerializer, LoadImageSerializerAll
from loadimage.models import LoadImageModel


class LoadImageViewList(APIView):

    parser_classes = [MultiPartParser, FormParser]
    
    def get(self, request, format=None):
        querySet=LoadImageModel.objects.all()
        serializer = LoadImageSerializerAll(querySet, many=True)
        return Response({"success":True, "data":serializer.data, "status":status.HTTP_200_OK})

    def post(self, request, *args, **kwargs):
        file = request.data['name_img']
        serializer = LoadImageSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            img = serializer.create(file)
            return Response({"success":True}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success":False, "data":NULL},status=status.HTTP_400_BAD_REQUEST)
        
class LoadImageView(APIView):
    
    def get_image(self, pk):
        try:
            return LoadImageModel.objects.get(pk=pk)
        except LoadImageModel.DoesNotExist:
            return 404

    def get(self, request, pk, format=None):
        image = self.get_image(pk)
        if image != 404:
            serializer = LoadImageSerializerAll(image, context={'reques':request})
            return Response({"success":True, "data":serializer.data}, status.HTTP_200_OK)
        else:
            return Response({"Error":'object not found'},status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        image = self.get_image(pk)
        file = request.data['name_img']
        if image != 404:
            serializer = LoadImageSerializer(image, data=request.data)
            if serializer.is_valid():
                try:
                    os.remove('assets/'+str(image.name_img))
                except os.error:
                    return Response({"success":False,"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
                image.name_img = file
                image.url_img='http://localhost:8000/assets/img/'+str(file)
                image.format_img= str(file).split('.')[1]
                image.save()
                return Response({"success":True},status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"success":False,"Error":'object not found'},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_image(pk)
        if image != 404:
            serializer = LoadImageSerializer(image, data=request.data)
            if serializer.is_valid():
                try:
                    os.remove('assets/'+str(image.name_img))
                except os.error:
                    return Response({"success":False,"Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
                image.delete()
                return Response({"success":True},status=status.HTTP_200_OK)
            else:
                return Response({"Error":'object not found'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error":'object not found'},status=status.HTTP_400_BAD_REQUEST)