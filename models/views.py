from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import APIKey
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def get_token(request):
    api_key = request.data.get('api_key')

    if not api_key:
        return Response({"detail": "API key is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        api_key_instance = APIKey.objects.get(key=api_key)
    except APIKey.DoesNotExist:
        return Response({"detail": "Invalid API key."}, status=status.HTTP_401_UNAUTHORIZED)

    user = api_key_instance.user
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    print(request.data)
    return Response({"message": "This is a protected view."})