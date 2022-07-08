from django import forms
from .models import Designation_Mst,Employee_Mst
from django.contrib.auth.forms import AuthenticationForm,UsernameField,_
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm,password_validation




YEARS= [x for x in range(1940,2021)]

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee_Mst
        fields=['first_name','last_name','designationld','date_of_joining','salary']
        widgets={
            
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'designationld':forms.Select(),
            'date_of_joining':forms.SelectDateWidget(years=YEARS),
            'salary':forms.NumberInput(attrs={'class':'form-control'}),

        
        }

class login(AuthenticationForm):
      username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'usernamepass','class':'form-control'}))
      password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )

class userresi(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
