from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from .models import CreateQuiz
import time
import datetime 


@api_view(['POST'])
def create(request):
    serialized = CreateQuizSerializer(data=request.data)
    if not serialized.is_valid():
        return Response({"Status": 404, "error": serialized.errors})
    serialized.save()
    return Response(serialized.data)


@api_view(['GET'])
def list_all(request,id):
    try:   
        data = CreateQuiz.objects.get(id=id)
        serializer = CreateQuizSerializer(data)
        return Response(serializer.data)
    except Exception as e:
         return Response({"invalid"})

@api_view(['GET'])
def Result(request, id):
    x = CreateQuiz.objects.get(id=id)
    serializer = CreateQuizSerializer(x)
    dt1 = datetime.datetime.now() 
    dt3 = datetime.timedelta(minutes=5)
    dt2 = dt1 + dt3
    dt2 = dt1.strftime("%H:%M:%S")
    if serializer.data["End_date"] < dt2:
        return Response(serializer.data["Answers"])
    else:
        return Response({"message":"wait till quiz ends"})
    
@api_view(['GET'])
def active(request):
    data = CreateQuiz.objects.all()
    serializer = CreateQuizSerializer(data, many=True)
    container = ''
    for i in serializer.data:
        dt1 = datetime.now()
        dt2 = dt1.strftime("%H:%M:%S")
        if dt2 < i["End_date"]:
            container = container + i["Questions"]
    return Response(container)


@api_view(['POST'])
def participate(request):
    serialized = ParticipateSerializer(data=request.data)
    if not serialized.is_valid():
        return Response({"status":404, "error":serialized.errors})
    serialized.save()
    return Response({"message":"Done!"})
         

# class Register(generics.ListAPIView, generics.UpdateAPIView):
#     queryset= CreateQuiz.objects.all()
#     serializer_class = CreateQuizSerializer
#     lookup_field= 'id'
    

@api_view(['PATCH'])
def update(request, id):
    user= CreateQuiz.objects.get(id= id)
    serializer = CreateQuizSerializer(user, request.data, partial = True)
    if not serializer.is_valid():
        return Response("Fuckkkkkkkkkk")
    serializer.save()
    return Response(serializer.data)