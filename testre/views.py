from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import UserSerializer

# Create your views here.
# def home(request):
#     return HttpResponse('hello')
def home(request):
    return render(request, 'index.html')



class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Loginvew(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        model = Loginmodel.objects.all()
        for i in model:
            print(i.username)
        
        # print("serializer",serializer)

        if serializer.is_valid():
            for data in model:
                if request.data['username'] in data.username:
                    print("filerd database")
                else:
                    serializer.save()
                    print("new comer")
            print("request data",request.data['username'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
