from django.db import models

# Create your models here.
class familiares(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
