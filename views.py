from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def ShowAllBooks(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewParticularBook(request,pk):
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(book,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def AddTheBook(request):
    serializer=BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def UpdateTheBookDetails(request,pk):
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def DeleteTheBook(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()

    return Response("Items with the given Id are delted successfully")