from rest_framework.views import APIView
from rest_framework.response import Response
from Register.serializer import UserSerializer
from rest_framework import status

# Create your views here.
class Register(APIView):
    def post(self, request, format = None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
