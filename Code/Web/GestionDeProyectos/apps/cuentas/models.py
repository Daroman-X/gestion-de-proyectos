from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    edad=models.PositiveIntegerField(null=True,blank=True)