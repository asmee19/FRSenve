
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('index1/',views.index1,name='index1'),
]