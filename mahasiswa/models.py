from statistics import mode
from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    semester = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
# def __str__(self):
#     return self.NIM
