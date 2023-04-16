from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import Seruse,postseralizer
from . models import MyUser,posts
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        # ...

        return token
class MyTokenObtainPair(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getUser(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)
@api_view(['POST'])
def giveuser(request):
    name = Seruse(data=request.data)
    print("out")
    if  name.is_valid():
        print("one")
        me = request.data['email']
        you =request.data['password']
        name.save()
        print("me")
        ui = MyUser.objects.filter(email =me).all()[0]
        ui.set_password(you)
        ui.save()
    elif not name.is_valid():
        return Response(name.data,300)
    return Response(name.data)
@api_view(['POST'])
def givepost(request):
    name = postseralizer(data=request.data)
    print("bme")
    if  name.is_valid():
        print("me")
        name.save()
    return Response(name.data)

@api_view(['GET'])
def givepostt(request):
    name = posts.objects.all()
    name2 = postseralizer(name,many=True)
    return Response(name2.data)

class Whynot(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format=None):
        print(request.data)
        serializer = postseralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletpostt(request,pk):
    name = posts.objects.get(id=pk)
    name.delete()
    return Response("item delete")    

