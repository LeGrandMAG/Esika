from django.db import models

# Create your models here.

class Adress(models.Model):
    address = models.TextField()
    lat = models.F