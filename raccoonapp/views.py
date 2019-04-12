from django.shortcuts import render
from raccoonapp.models import Raccoon,Photo,Yummy
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView,UpdateView,DetailView
# Create your views here.
from raccoonapp.forms import SeachForm,CalcForm,YammuFrom
import json
def home_view(request):
    raccoon_list = Raccoon.objects.all()
    context={'raccoon_list':raccoon_list}
    context['form'] = CalcForm()
    response  = render(request,'home.html',context=context)
    return response

class RaccoonListView(ListView):
    model = Raccoon
    def get_queryset(self,*args,**kwargs):
        queryset = super(RaccoonListView,self).get_queryset(*args,**kwargs)
        if 'raccoon_name' in self.request.POST:
            #name = self.request.GET['raccoon_name']
            name = self.request.POST['raccoon_name']
            queryset =queryset.filter(name__icontains=name)
        return queryset


    def get_context_data(self,*args,**kwargs):
        context = super(RaccoonListView,self).get_context_data(*args,**kwargs)
        return context

class RaccoonDetailView(DetailView):
    model =Raccoon
    def get_context_data(self,*args,**kwargs):
        context = super(RaccoonDetailView,self).get_context_data(*args,**kwargs)
        context['data'] =self.kwargs['data']
        return context
class RaccoonUpdateView(UpdateView):
    model =Raccoon
    fields= '__all__'


def yammy_view(request):
    context={}
    if request.GET:
        form = YammuFrom(request.GET)
        context['form'] = form
        if form.is_valid():
            yummy = Yummy.objects.filter(raccoon=form.cleaned_data['raccoon']).filter(date=form.cleaned_data['date'])
            context['yummy'] = yummy

    else:
        context['form'] = YammuFrom()
    response  = render(request,'yummy.html',context=context)
    return response

def yummy_json(request):

    if request.POST:
        form = YammuFrom(request.POST)
        if form.is_valid():
            yummy = Yummy.objects.filter(raccoon=form.cleaned_data['raccoon']).filter(date=form.cleaned_data['date'])
    ls = []
    for y in yummy:
        ls.append({'name':y.name})

    #date= json.dumps(ls)
    return JsonResponse(ls,safe=False)


