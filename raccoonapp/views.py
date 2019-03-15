from django.shortcuts import render
from raccoonapp.models import Raccoon,Photo
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView,UpdateView,DetailView
# Create your views here.

def home_view(request):
    raccoon_list = Raccoon.objects.all()
    context={'raccoon_list':raccoon_list}
    response  = render(request,'home.html',context=context)
    return response

class RaccoonListView(ListView):
    model = Raccoon
    def get_queryset(self,*args,**kwargs):
        queryset = super(RaccoonListView,self).get_queryset(*args,**kwargs)
        if 'raccoon_name' in self.request.GET:
            name = self.request.GET['raccoon_name']
            queryset =queryset.filter(name__icontains=name)
        return queryset


    def get_context_data(self,*args,**kwargs):
        context = super(RaccoonListView,self).get_context_data(*args,*kwargs)
        return context

class RaccoonDetailView(DetailView):
    model =Raccoon
class RaccoonUpdateView(UpdateView):
    model =Raccoon
    fields= '__all__'
