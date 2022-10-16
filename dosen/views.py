from django.shortcuts import render
from . models import Dosen

# Create your views here.
def dosenmtk(request):
    dosen = Dosen.objects.all()
    konteks = {
        'dataDosen': dosen,
    }
    return render(request, 'dosen.html', konteks)