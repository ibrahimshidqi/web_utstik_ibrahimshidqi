from statistics import mode
from django.db import models

# Create your models here.
class Penelitian(models.Model):
    tahun_akademik = models.CharField(max_length=200)
    judul_penelitian = models.CharField(max_length=200)
    nama_ketua_tim = models.CharField(max_length=200, null=True)
    kepakaran_ketua_tim = models.CharField(max_length=200)
    nama_dan_identitas_dosen_anggota_penelitian = models.CharField(max_length=200)
    nama_dan_identitas_mahasiswa_yang_dilibatkan = models.CharField(max_length=200)
    
# def __str__(self):
#     return self.NIM
