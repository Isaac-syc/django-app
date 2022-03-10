
from rest_framework import serializers
from django.contrib.auth.models import User
from perfil.models import PerfilModel


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilModel
        fields = ('__all__')
        
    def create(self, img, user):
        PerfilModel.objects.create(name_img=img,user=user)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','first_name','last_name','email')