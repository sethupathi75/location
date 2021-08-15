from django.db import models
from django.db.models.fields import CharField, EmailField, TextField


class login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=12)


# Create your models here.
