from rest_framework import serializers
from .models import User

class User_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password_hash', 'activated', 'role', 'date_of_birth', 'last_login', 'date_of_creation')