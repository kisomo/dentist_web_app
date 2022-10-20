
from django import forms 
from django.forms import ModelForm
from . models import Dentist, Venue

'''
class DentistForm(forms.Form):
    Hospital_choices = ((1,"Bellevile"),(2,"Verona"),(3,"Glenridge"))
    fname = forms.CharField()
    lname = forms.CharField()
    age = forms.IntegerField()
    hospital = forms.ChoiceField(choices=Hospital_choices)
    date_of_birth = forms.DateField()
'''


class DentistForm2(ModelForm):
    class Meta:
        model = Dentist 
        #fields = "__all__"
        fields = ("fname","lname","qualification","experience_yrs")
        widgets = {
            'fname': forms.TextInput(attrs= {'class':'form-control'}),
            'lname': forms.TextInput(attrs= {'class':'form-control'}),
            'qualification': forms.Select(attrs= {'class':'form-control'}),
            'experience_yrs': forms.TextInput(attrs= {'class':'form-control'}),
        }

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ("vname","address","zip_code","phone","web","email_address")
        widgets = {
            'vname': forms.TextInput(attrs= {'class':'form-control'}),
            'address': forms.TextInput(attrs= {'class':'form-control'}),
            'zip_code': forms.TextInput(attrs= {'class':'form-control'}),
            'phone': forms.TextInput(attrs= {'class':'form-control'}),
            'web': forms.TextInput(attrs= {'class':'form-control'}),
            'email_address': forms.TextInput(attrs= {'class':'form-control'}),
        }

