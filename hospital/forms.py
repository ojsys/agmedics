from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class AddPatientForm(forms.ModelForm):
    
    class Meta: 
        model = Patient
        fields = ('hospital_no','firstname', 'lastname', 'date_of_birth', 'age', 'address', 'mobile_number', 'ailment',)
        labels = {
            'hospital_no':'Hospital Number',
            'firstname': 'First Name', 
            'lastname': 'Last Name', 
            'date_of_birth': 'Date of Birth', 
            'age': 'Age', 
            'address': 'Address', 
            'mobile_number': 'Mobile Number', 
            'ailment': 'Ailment'
        }
        widgets = {
            'hospital_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hospital Number'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'date_of_birth': DateInput(),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter address'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Phone Number'}),
            'ailment': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ailment'}),
        }

