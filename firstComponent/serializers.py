from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from firstComponent.models import FristModel

class FirstComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FristModel
        fields= ('__all__')
        
