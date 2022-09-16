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
                             status=status.HTTP_400_BAD_REQUEST))

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

        return(Response({'status':"Success",'candidate':serializer.data},status=status.HTTP_200_OK))

    def put(self, request,pram=None ,pk=None,udata=None, format=None):
        candidates = user_data.objects.all()
        print(f"-----------Value of pk------->{pk}")
        ids_available = [data.id for data in candidates]

        if (pk is not None) and (pk in ids_available) and (pram is not None):
            query_set = candidates.get(id=pk)
            query_set.pram=udata
            query_set.save()
            serializer = UserDataSerializers(query_set, many=False)

        return (Response({'status': "Success", 'candidate': serializer.data}, status=status.HTTP_202_ACCEPTED))


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
