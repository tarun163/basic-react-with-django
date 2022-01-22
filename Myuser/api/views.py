from django.shortcuts import render
from .models import * 
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch') 
@permission_classes((permissions.AllowAny,))
class Usersystem(APIView):
    def get(self, request):
        data = CustomUser.objects.all()
        serializerData = UserSerializer(data, many=True )
        return Response(serializerData.data)
    
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
            
    def put(self, request, pk):
        id = pk
        data = request.data
        user = CustomUser.objects.get(pk=id)
        serializer = UserSerializer(user, data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
               
    def delete(self, request, pk):
        id = pk
        user = CustomUser.objects.get(pk=id).delete()
        return Response({"msg":"data deleted successfully"})
    
    def patch(self, request, pk):
        id = pk
        user = CustomUser.objects.get(pk=id)
        serializer = UserSerializer(user)        
        return  Response(serializer.data)
        
        
                
     