from django.shortcuts import render
from . models import Mahasiswa

# Create your views here.
def mahasiswamtk(request):
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'mahasiswa.html', konteks)
