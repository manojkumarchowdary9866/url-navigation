from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[ 
    path('p1url1/',p1url1,name='p1url1'),
]