from django.urls import re_path

from perfil.views import Perfil, UserView


urlpatterns = [
    re_path(r'^v1/user/(?P<pk>\d+)/$', UserView.as_view()),       
    re_path(r'^v1/profile/(?P<pk>\d+)/$', Perfil.as_view()),       
]