from django.urls import re_path

from register.views import Register


urlpatterns = [
       
    re_path(r'', Register.as_view()),       
]