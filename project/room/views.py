from django.shortcuts import render
from .forms import SearchForm
from .models import Room


# Create your views here.
def index(request):
  room =Room.objects.all()
  return render(request, 'index.html', {'room':room})

def contact(request):
    if request.method == "POST":
        searched = request.POST['searched']
        room = Room.objects.filter(price__contains=searched)
        return render(request, 'contact.html', {'searched':searched,'room':room})
    else:
        return render(request, 'contact.html', {})

# def contact(request):
#     if request.method == "POST":
#         if 'searched' in request.POST:
#             searched = request.POST['searched']
#             room = Room.objects.filter(name__contains=searched)
#             return render(request, 'contact.html', {'searched': searched},{'room':room})
#         else:
#             return render(request, 'contact.html', {})
   

   







    
