

from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import explorer



def demo(request):
    obj=Place.objects.all()
    obj1=explorer.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# Create your views here.
