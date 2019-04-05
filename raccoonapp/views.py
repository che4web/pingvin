from django.shortcuts import render
from raccoonapp.models import Raccoon,Photo
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView,UpdateView,DetailView
# Create your views here.
from raccoonapp.forms import SeachForm,CalcForm

def home_view(request):
    raccoon_list = Raccoon.objects.all()
    context={'raccoon_list':raccoon_list}
    context['form'] = CalcForm()
    if request.GET:
        form  = CalcForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            operator = request.GET['operator']
            if operator =="mult":
                res = a*b
            if operator == "plus":
                res = a+b
            context['res']=res
        context['form']=form

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
