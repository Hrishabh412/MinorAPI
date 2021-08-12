from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse, HttpResponse

from rest_framework.parsers import JSONParser
from upwork.models import Student
from .serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from upwork import serializers
from rest_framework import generics
from rest_framework import mixins

class StudentGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= StudentSerializer
    queryset=Student.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)