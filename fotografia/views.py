from django.shortcuts import render
from fotografia.models import Corretor

def index(request):
    return render(request, 'fotografia/index.html')

def list_corretores(request):
    corretores = Corretor.objects.all()
    return render(request, 'fotografia/list_corretores.html', {"obj": corretores})
