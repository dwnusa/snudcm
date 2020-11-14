from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
# from sntemplate.eval_tf import eval
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!")


class index_as_view(APIView):
    def get(self, request, format=None):
        return Response(data="index world!", status=status.HTTP_200_OK)


class Hello(APIView):
    # def get(self, format=None):
    def get(self, request, format=None):
        return Response(data="Hello world!", status=status.HTTP_200_OK)

