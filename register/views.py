from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from user.serializer import User_Serializers
from django.contrib.auth.hashers import make_password
from user.password_validator import NumberValidator, UppercaseValidator, LowercaseValidator, SymbolValidator

# Create your views here.

def register(request):
    if request.method == 'POST':

        try:
            
            NumberValidator.validate(request.data['password'])
            UppercaseValidator.validate(request.data['password'])
            LowercaseValidator.validate(request.data['password'])
            SymbolValidator.validate(request.data['password'])
        except ValidationError:

            Response(status=status.HTTP_400_BAD_REQUEST, data=ValidationError.get_help_text())

        request.data['password_hash'] = make_password(request.data['password'])
        del request.data['password']

        user_serializer = User_Serializers(data=request.data)
        if not user_serializer.is_valid():
            
            return Response(status=status.HTTP_400_BAD_REQUEST, data=user_serializer.error_messages)

        user_serializer.save()
        return Response(status=status.HTTP_201_CREATED)

def register_view(request):
    pass