from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
# from sntemplate.eval_tf import eval
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pydicom
import numpy as np
from django.http import FileResponse
import os, io, zipfile
import copy
from pydicom.filebase import DicomFileLike
from io import BytesIO
import time


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index!")
#
#
# class index(APIView):
#     def get(self, request, format=None):
#         return Response(data="index world!", status=status.HTTP_200_OK)


class Splitter(APIView):
    def get(self, request, format=None):
        return Response(data="Welcome, Dicom Magician", status=status.HTTP_200_OK)

    def post(self, request, format=None):

        myfiles = request.FILES.getlist('myfiles')
        # Check if file attached
        if not myfiles:
            return Response(data="Files are not attached correctly", status=status.HTTP_400_BAD_REQUEST)
        Nfiles = len(myfiles)
        # Create zip
        zip_buffer = io.BytesIO()
        zip_file = zipfile.ZipFile(zip_buffer, 'w')
        for file in myfiles:
            # print(file.name)
            ds = pydicom.dcmread(file)
            Nframes = ds.NumberOfFrames
            print(Nframes)
            frames = ds.pixel_array

            filename = file.name.split('.')[0]

            frame_list = list(enumerate(frames))
            for idx, frame in frame_list:
                framename = filename+"("+str(idx)+")"+".dcm"
                print(frame.shape)
                milliseconds = str(round(time.time() * 1000))
                print(milliseconds)
                tp = copy.deepcopy(ds)

                tp.NumberOfFrames = "1"
                tp.PixelData = frame
                tp.StudyInstanceUID = tp.StudyInstanceUID[:-len(milliseconds)-1]+"."+milliseconds

                buffer = io.BytesIO()
                # create a DicomFileLike object that has some properties of DataSet
                memory_dataset = DicomFileLike(buffer)
                # write the dataset to the DicomFileLike object
                pydicom.dcmwrite(memory_dataset, tp)
                # to read from the object, you have to rewind it
                memory_dataset.seek(0)
                # read the contents as bytes
                ds_bytes = memory_dataset.read()
                zip_file.writestr(framename, ds_bytes)

        # Return zip
        zip_file.close()
        response = HttpResponse(zip_buffer.getvalue())
        response['Content-Type'] = 'application/x-zip-compressed'
        response['Content-Disposition'] = 'attachment; filename=singleframes.zip'
        return response