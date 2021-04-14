from django.shortcuts import render

# Create your views here.

from index.models import songs

def player(request):
  
  cont = {}
  list = songs.objects.filter(name="")
  list2 = []
  
  if request.method == "POST":
    
    title = request.POST.get("title")

    current = songs.objects.filter(name=title)
    print(current)
    
    for curr in current:
      words = curr.desc
      wordlist = words.split(" & ")
      
      for half in wordlist:
        list |= songs.objects.filter(desc__contains=half)
     
      list = list.distinct()
     
      for each in list:
        if not each.name == curr.name:
          list2.append(each)
      

    cont ={"current" : current, "queue" : list2}
  
  return render(request,'player.html',cont)
