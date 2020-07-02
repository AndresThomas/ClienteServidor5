from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404


# Create your views here.
from Example1.models import Example1
from Example1.serializer import Example1Serializers

class ExampleList(APIView):
    def get(self, request, format = None):
        print("Get in 15")
        queryset = Example1.objects.all()
        serializer = Example1Serializers(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = Example1Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)

class ExampleDetail(APIView):
    def get_object(self,id):
        try:
            return Example1.objects.get(pk = id)
        except Example1.DoesNotExist:
            return 404
    
    def get(self, request, id ,format = None):
        example_object = self.get_object(id) 
        if example_object != 404:
            serializer = Example1Serializers(example_object)
            return Response(serializer.data)
        return Response("No hay datos")
    
    def put(self,request,id,format = None):
        modify = self.get_object(id)

        if modify != 404:
            serializer = Example1Serializers(modify, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response("Ingrese un formato valido")
        else:
            return Response("Este elemento no existe")

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user != 404:
            user.delete()
            return Response('Elemento borrado', status=status.HTTP_200_OK)
        else:
            return Response(user, status=status.HTTP_404_NOT_FOUND)