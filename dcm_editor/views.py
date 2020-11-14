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


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!")


class index_as_view(APIView):
    def get(self, request, format=None):
        return Response(data="index world!", status=status.HTTP_200_OK)


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
        # return Response(data="Welcome, Splitter post view", status=status.HTTP_200_OK)

class Splitter_reconstruction(APIView):
    # def get(self, format=None):
    def get(self, request, format=None):
        current_path = os.getcwd()
        # file_name = "temp1.dcm"
        # file_path = os.path.join(current_path, file_name)
        # ds1 = pydicom.dcmread(file_path)
        # buffer1 = io.BytesIO()
        # # create a DicomFileLike object that has some properties of DataSet
        # memory_dataset1 = DicomFileLike(buffer1)
        # # write the dataset to the DicomFileLike object
        # pydicom.dcmwrite(memory_dataset1, ds1)
        # # to read from the object, you have to rewind it
        # memory_dataset1.seek(0)
        # # read the contents as bytes
        # ds_bytes1 = memory_dataset1.read()
        #
        # buffer3 = io.BytesIO()
        # zip_file = zipfile.ZipFile(buffer3, 'w')
        # zip_file.writestr(file_name, ds_bytes1)
        # zip_file.close()
        # # Return zip
        # response = HttpResponse(buffer3.getvalue())
        # response['Content-Type'] = 'application/x-zip-compressed'
        # response['Content-Disposition'] = 'attachment; filename=album.zip'
        # return Response(data=response, status=status.HTTP_200_OK)
        return Response(data="Hello world splitter!", status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # extraction of information from request
        # userId = request.user.id
        myfiles = request.FILES.getlist('myfiles')
        # Check if file attached
        if not myfiles:
            return Response(data="Files are not attached correctly", status=status.HTTP_400_BAD_REQUEST)
        myfile = myfiles[0]
        temp1 = copy.deepcopy(myfile)
        temp2 = copy.deepcopy(myfile)
        ds1 = pydicom.dcmread(temp1)
        ds2 = pydicom.dcmread(temp2)
        strMyfile = myfile.read()
        # strMyfile = copy.deepcopy(myfile.read())
        print(ds1)
        pixel_array1, pixel_array2 = ds1.pixel_array[0, :, :], ds1.pixel_array[1, :, :]
        # print(ds1)
        ds1.NumberOfFrames = "1"
        ds1.PixelData = pixel_array1
        ds1.StudyInstanceUID = '1.2.124.113532.192.147.106.101.20080114.92117.7870431'

        ds2.NumberOfFrames = "1"
        ds2.PixelData = pixel_array2
        ds2.StudyInstanceUID = '1.2.124.113532.192.147.106.101.20080114.92117.7870432'

        buffer1 = io.BytesIO()
        # create a DicomFileLike object that has some properties of DataSet
        memory_dataset1 = DicomFileLike(buffer1)
        # write the dataset to the DicomFileLike object
        pydicom.dcmwrite(memory_dataset1, ds1)
        # to read from the object, you have to rewind it
        memory_dataset1.seek(0)
        # read the contents as bytes
        ds_bytes1 = memory_dataset1.read()

        buffer2 = io.BytesIO()
        # create a DicomFileLike object that has some properties of DataSet
        memory_dataset2 = DicomFileLike(buffer2)
        # write the dataset to the DicomFileLike object
        pydicom.dcmwrite(memory_dataset2, ds2)
        # to read from the object, you have to rewind it
        memory_dataset2.seek(0)
        # read the contents as bytes
        ds_bytes2 = memory_dataset2.read()



        filename1 = "temp1.dcm"
        filename2 = "temp2.dcm"
        # Create zip
        buffer3 = io.BytesIO()
        zip_file = zipfile.ZipFile(buffer3, 'w')
        zip_file.writestr(filename1, ds_bytes1)
        zip_file.writestr(filename2, ds_bytes2)
        zip_file.close()
        # Return zip
        response = HttpResponse(buffer3.getvalue())
        response['Content-Type'] = 'application/x-zip-compressed'
        response['Content-Disposition'] = 'attachment; filename=album.zip'
        return response
        # current_path = os.getcwd()
        # ds.save_as(current_path + "/IM11.dcm", write_like_original=False)
        # response = FileResponse(document.file, )
        # response["Content-Disposition"] = "attachment; filename=" + file_name

        # Get filename from url
        filename = "temp.dcm"
        # Create zip
        buffer2 = io.BytesIO()
        zip_file = zipfile.ZipFile(buffer2, 'w')
        zip_file.writestr(filename, strMyfile)
        zip_file.close()
        # Return zip
        response = HttpResponse(buffer2.getvalue())
        response['Content-Type'] = 'application/x-zip-compressed'
        response['Content-Disposition'] = 'attachment; filename=album.zip'
        return response
        # return Response(data=myfile, status=status.HTTP_200_OK)
