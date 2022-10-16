from django.shortcuts import render
from . models import Penelitian


# Create your views here.
def penelitianmtk(request):
    penelitian = Penelitian.objects.all()
    konteks = {
        'dataPenelitian': penelitian,
    }
    return render(request, 'penelitian.html', konteks)
