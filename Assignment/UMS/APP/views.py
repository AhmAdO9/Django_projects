from rest_framework.decorators import api_view, authentication_classes, permission_classes
from APP.serializers import *
from rest_framework.response import Response
from .models import TO_DO
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def authentication(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username= username, password = password)
    if user:
        token, _ = Token.objects.get_or_create(user = user)
        return Response(str(token))
    serializer = UserSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors)
    serializer.save()
    user1 = User.objects.get(username = serializer.data['username'])
    token, _ = Token.objects.get_or_create(user= user1)
    return Response(str(token))



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def read_all(request):
    obj = TO_DO.objects.all()
    serializer = ListSerializer(obj, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def create(request): 
    serializer = ListSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def read_id(request, id):
  try:  
    obj = TO_DO.objects.get(id= id)
    serializer = ListSerializer(obj)
    return Response(serializer.data)
  except Exception:
      return Response({"error":"invalid id"})

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def update(request, id):
   try:
    obj = TO_DO.objects.get(id = id)
    serializer = ListSerializer(obj, data=request.data, partial= True)
    if not serializer.is_valid():
        return Response(serializer.errors)
    serializer.save()
    return Response(serializer.data)
   except Exception:
      return Response({"error":"invalid id"})


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def delete_id(request, id): 
   try:
    obj = TO_DO.objects.get(id= id)
    obj.delete()
    return Response({"message":"Deleted"})
   except Exception:
      return Response({"error":"invalid id"})
   



