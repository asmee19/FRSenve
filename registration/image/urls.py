
from django.urls import path
from . import views

urlpatterns = [
    path('index2/',views.index2,name='index2'),
    path("",views.index2,name="home1"),
]