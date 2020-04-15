from django import forms
from .models import Tourist
from django.contrib.auth.models import User

class TuserForm(forms.ModelForm):
	username=forms.CharField(label=("Username"),widget=forms.TextInput( attrs={'placeholder':
                                          ('Username'),
                                          'autofocus': 'autofocus','required':'true'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':('password')}))
	email = forms.EmailField(max_length=254)

	class Meta:
		model=User
		fields=('username','email','password')

class InterestsForm(forms.ModelForm):
	class Meta:
		model=Tourist
		fields=('interest_rate','locations','languages')
