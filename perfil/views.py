from asyncio.windows_events import NULL
from django.shortcuts import render
import os
from rest_framework.response import Response
from perfil.serializers import PerfilSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from perfil.models import PerfilModel



class Perfil(APIView):
    permission_classes = (AllowAny,)
    
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return 404

    def get_profile(self, pk):
        try:          
            return PerfilModel.objects.get(user_id = pk)
        except PerfilModel.DoesNotExist:
            return 404
    
    def get(self, request,pk,format=None):
        perfil = self.get_profile(pk)
        if perfil!=404:
            serializer=PerfilSerializer(perfil)
            return Response({"success":True, "data":serializer.data}, status.HTTP_200_OK)
        else: return Response({"success":False}, status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk, format=None):
        perfil = self.get_profile(pk)
        user = self.get_user(pk)
        if user!=404:    
            if perfil != 404:
                string_image = str(perfil.name_img)                           
                try:
                    os.remove('assets/'+string_image)
                except os.error:
                    return Response({"success":False}, status.HTTP_400_BAD_REQUEST)
                perfil.name_img=request.data['name_img']
                perfil.save()
                serializer = PerfilSerializer(perfil)
                return Response({"success":True, "data":serializer.data}, status.HTTP_200_OK)
            else: 
                serializer = PerfilSerializer(data=request.data, context={'request':request})
                if serializer.is_valid():
                    name_img = request.data['name_img']
                    serializer.create(name_img,user)
                    return Response({"success":True, "data":serializer.data}, status.HTTP_200_OK)
                else: return Response({"success":False}, status.HTTP_400_BAD_REQUEST)
        else: return Response({"success":False}, status.HTTP_400_BAD_REQUEST)
        
class UserView(APIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return 404
    
    def get(self, request,pk,format=None):
       user = self.get_user(pk)
       if user!=404:
            serializer=UserSerializer(user)
            return Response({"success":True, "data":serializer.data}, status.HTTP_200_OK)
       else: return Response({"success":False}, status.HTTP_400_BAD_REQUEST)
       
    def put(self, request, pk, format=None):

        data = request.data
        user = User.objects.filter(id = pk)
        user.update(username = data.get('username'))
        user.update(first_name = data.get('first_name'))
        user.update(last_name = data.get('last_name'))
        user.update(email = data.get('email'))
        return Response({"success":True, "data":user.values()[0]}, status.HTTP_200_OK)
    

    
       
        
       
    