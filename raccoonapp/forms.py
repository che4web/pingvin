from django import forms

class BootstrapForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super(BootstrapForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})


class SeachForm(forms.Form):
    raccoon_name = forms.CharField(label='Имя енота', max_length=3)
    raccoon_name = forms.CharField(label='Имя енота', max_length=3)

class CalcForm(BootstrapForm):
    a = forms.IntegerField(label='a')
    b = forms.IntegerField(label='b')

