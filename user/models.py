from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(Enum):
    admin = 'admin'
    guest = 'guest'
    user = 'user'

class User(AbstractUser):
    
    username = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=100, choices=[(role, role.value) for role in Role], default=Role.user)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    REQUIRED_FIELDS = []
