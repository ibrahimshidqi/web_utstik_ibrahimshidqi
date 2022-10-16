from statistics import mode
from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    jabatan = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
# def __str__(self):
#     return self.NIP