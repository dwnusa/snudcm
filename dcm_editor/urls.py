from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index_as_view.as_view(), name='index_as_view'),
    path('hello', views.Hello.as_view(), name='hello'),
]