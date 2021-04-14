from django.shortcuts import render

# Create your views here.

from index.models import songs

def search(request):
  
  cont ={}
  
  output = songs.objects.filter(name="")
  
  if request.GET.get('inpname'):
    inpname = request.GET.get('inpname')
    
    output1 = songs.objects.filter(desc__contains=inpname)
    output2 = songs.objects.filter(name__contains=inpname)
      
    output |= output1 
    output |= output2
      
    cont["results"] = output.distinct()
    
    return render(request,"search.html",cont)