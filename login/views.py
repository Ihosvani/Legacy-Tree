from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from user.serializer import User_Serializers
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def create_jwt(username, email):
    pass

def get_jwt_data(JWT):
    pass

def login(request):
    if request.method == 'POST':
        #user not found by email
        try:
            user = User.objects.filter(email=request.data[0])
        except User.DoesNotExist:
            return Response(data='An user with that email does not exists in our database', status=status.HTTP_401_UNAUTHORIZED)
        
        user_serializer = User_Serializers(user)
        hashed_password = make_password(request.data[1])

        #user found but password doesn't match
        if not check_password(hashed_password, user_serializer.data['password_hash']):
            return Response(data='Wrong password', status=status.HTTP_404_NOT_FOUND)
        
        #if succesful will send [jwt, user]
        return Response([create_jwt(user_serializer.data['username'], user_serializer.data['email'], user_serializer.data.values)], status=status.HTTP_202_ACCEPTED)

def login_view(request, *args, **kwargs):
    return render(request, 'login.html', {})
