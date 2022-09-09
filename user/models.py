from django.db import models

# Create your models here.


class User(models.Model):
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password_hash = models.CharField()
    activated = models.BooleanField(default=False)

    class Role(models.TextChoices):
        ADMIN = 'admin', _('admin')
        GUEST = 'guest', _('guest')
        USER = 'user', _('user')
    
    role = models.CharField(choices=Role.choices, default=Role.USER)