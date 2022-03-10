from django.urls import path, re_path
from django.conf.urls import include


from firstComponent.views import PrimerTablaList,FirstView

urlpatterns = [
    re_path(r'^lista/$', PrimerTablaList.as_view()),    
    re_path(r'^lista/(?P<pk>\d+)/$', FirstView.as_view()),
]
