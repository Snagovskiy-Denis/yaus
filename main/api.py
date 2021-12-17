from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import URLSerializer


class CreateShortURL(APIView):

    def post(self, request, format=None):
        new_url_data = {
            'full': request.data.get('url'),
            'short': request.data.get('name', '')
        }
        serializer = URLSerializer(data=new_url_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        url = serializer.save()
        return Response(url.short, status=status.HTTP_200_OK)
