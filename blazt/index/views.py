from django.shortcuts import render

# Create your views here.

from .models import songs

def home(request):
  
  cont = {} 
  
  objs = songs.objects.all()
  cont["objs"] = objs

  return render(request,'home.html',cont)