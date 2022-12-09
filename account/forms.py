from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

USER_CHOICES = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('R', 'Receptionist'),
    ('HR', 'HR'),
    ('PX', 'Pharmacist'),
    ('L', 'Lab Techician'),
]

class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder':'Username'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    user_type = forms.ChoiceField(choices=USER_CHOICES, required=True, widget=forms.RadioSelect)
    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "user_type")
        model = get_user_model()
        labels = {
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'username': 'Username', 
            'email': 'Email', 
            'password1':'Password', 
            'password2':'Confirm Password', 
            'user_type':'User Type',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password'}),
            'password2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),
            'user_type': forms.RadioSelect(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))