
from django import forms 
from django.forms import ModelForm
from . models import Dentist

class DentistForm(forms.Form):
    Hospital_choices = ((1,"Bellevile"),(2,"Verona"),(3,"Glenridge"))
    fname = forms.CharField()
    lname = forms.CharField()
    age = forms.IntegerField()
    hospital = forms.ChoiceField(choices=Hospital_choices)
    date_of_birth = forms.DateField()



class DentistForm2(ModelForm):
    class Meta:
        model = Dentist 
        #fields = "__all__"
        fields = ("fname","lname","qualification","experience_yrs")

