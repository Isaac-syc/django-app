from django.urls import path, include, re_path
from django.contrib.auth.models import User
from perfil.models import PerfilModel
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import AllowAny
from django.views.static import serve
from django.conf import settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet),



urlpatterns = [
    path('', include(router.urls)),
    #Login
    re_path(r'^api/', include('Login.urls')),
    
    #Register
    re_path(r'^api/Register', include('register.urls')),
    
    #perfil
    re_path(r'^api/Profile/', include('perfil.urls')),
    
    
    #firstComponent
    re_path(r'^api/primer_componente/', include('firstComponent.urls')), 
    
    #images
    re_path(r'^api/load-images/', include('loadimage.urls')),
    
    re_path(r'assets/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
