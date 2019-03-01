from django.shortcuts import render
from raccoonapp.models import Raccoon

from django.views.generic import ListView
# Create your views here.
class RacconList(ListView):
    model= Raccoon
def crt_view(request):
    print(request.GET['crt'])
    return render(request,'test_ssl.html')
