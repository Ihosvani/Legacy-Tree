from datetime import datetime
from enum import Enum
from django.db import models

# Create your models here.

class Role(Enum):
    admin = 'admin'
    guest = 'guest'
    user = 'user'

class User(models.Model):
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    activated = models.BooleanField(default=False)
    role = models.CharField(max_length=5, choices=[(role, role.value) for role in Role], default=Role.user)
    date_of_birth = models.DateTimeField()
    last_login = models.DateTimeField()
    date_of_creation = models.DateTimeField(default=datetime.now())