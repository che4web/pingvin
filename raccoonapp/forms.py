from django import forms

class SeachForm(forms.Form):
    raccoon_name = forms.CharField(label='Имя енота', max_length=3)
