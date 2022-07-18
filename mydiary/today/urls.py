 
from django.urls import path
from today import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('about/',views.about),
]
