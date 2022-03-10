from django.urls import path, re_path
from django.conf.urls import include


from loadimage.views import LoadImageViewList, LoadImageView

urlpatterns = [       
    re_path(r'^img/$', LoadImageViewList.as_view()),
    re_path(r'^img/(?P<pk>\d+)/$', LoadImageView.as_view()),
    
]
