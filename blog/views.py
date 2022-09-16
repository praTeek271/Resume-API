# from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from .models import user_data

from .serializers import UserDataSerializers
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class user_dataAPI(APIView):

    def post(self, request, format=None):
        serializer = UserDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return (
                Response({'msg': 'Successfully created user_data', 'status': 'Success', 'Candidate': serializer.data},
                         status=status.HTTP_201_CREATED))
        else:
            return (Response({'msg': 'Not Able to create user_data', 'status': 'Faliure', 'Candidate': serializer.data},
                             status=serializer.error_messages))

    def get(self, request,pk=None,format=None):
        candidates = user_data.objects.all()
        print(f"-----------Value of pk------->{pk}")
        serializer = UserDataSerializers(candidates, many=True)

        ids_available = [data.id for data in candidates]

        if (pk is not None) and (pk in ids_available):
            query_set=candidates.get(id=pk)
            serializer = UserDataSerializers(query_set, many=False)


        return (Response({'candidate': serializer.data}, status=status.HTTP_200_OK))

    def delete(self, request,pk=None,format=None):
        candidates = user_data.objects.all()
        print(f"-----------Value of pk------->{pk}")
        serializer = UserDataSerializers(candidates, many=True)

        ids_available = [data.id for data in candidates]

        if (pk is not None) and (pk in ids_available):
            query_set=candidates.get(id=pk)
            query_set.delete()
            query_set.save()

            serializer = UserDataSerializers(query_set, many=False)

        return(Response({'status':"Success DELETED",'candidate':serializer.data},status=status.HTTP_200_OK))

    def put(self, request,pram=None ,pk=None,udata=None, format=None):
        candidates = user_data.objects.all()
        # print(f"-----------Value of pk------->{pk}")
        # print(f"-----------Value of udata------->{udata}")
        # print(f"-----------Value of pram------->{pram}")
        ids_available = [data.id for data in candidates]

        if (pk is not None) and (pk in ids_available) and (pram is not None) and (udata is not None):
            query_set = candidates.get(id=pk)
            if pram=='username':query_set.username=udata
            if pram=='DOB':query_set.DOB=udata
            if pram=='gender':query_set.gender=udata
            if pram=='email':query_set.email=udata
            if pram=='resume':query_set.resume=udata
            if pram=='state':query_set.state=udata
            
            query_set.save()
            serializer = UserDataSerializers(query_set, many=False)

        return (Response({'status': "Success uPDATED", 'candidate': serializer.data}, status=status.HTTP_202_ACCEPTED))


class User_dataCreateView(generics.ListCreateAPIView):
    queryset = user_data.objects.all()
    serializer_class = UserDataSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class User_dataRetrive(generics.RetrieveAPIView):
    queryset = user_data.objects.all()
    serializer_class = UserDataSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

class User_dataDelete(generics.DestroyAPIView):
    queryset = user_data.objects.all()
    serializer_class = UserDataSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
class User_dataUpdate(generics.UpdateAPIView):
    queryset = user_data.objects.all()

    serializer_class = UserDataSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
