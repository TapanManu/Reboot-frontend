from django import forms
from .models import Guides
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username=forms.CharField(label=("Username"),widget=forms.TextInput( attrs={'placeholder':
                                          ('Username'),
                                          'autofocus': 'autofocus','required':'true'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':('password')}))
	email = forms.EmailField(max_length=254)

	class Meta:
		model=User
		fields=('username','email','password')

class GuserForm(forms.ModelForm):
	username=forms.CharField(label=("Username"),widget=forms.TextInput( attrs={'placeholder':
                                          ('Username'),
                                          'autofocus': 'autofocus','required':'true'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':('password')}))
	email = forms.EmailField(max_length=254)

	class Meta:
		model=User
		fields=('username','email','password')

class GuidesForm(forms.ModelForm):
	cuisines=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the cuisines you know in your locality')}))
	arts=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the arts you know in your locality')}))
	hotspots=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the hotspots you know in your locality')}))
	culture=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the culture you know in your locality')}))
	class Meta:
		model=Guides
		fields=('g_contact','base_rate','operating_level','location','known_languages','cuisines','arts','hotspots','culture',)

#class SkillsForm(forms.ModelForm):
#	class Meta:
#		model=Skills
#		fields=('known_languages'),

#class CommunityForm(forms.ModelForm):
#	cuisines=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the cuisines you know in your locality')}))
#	arts=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the arts you know in your locality')}))
#	hotspots=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the hotspots you know in your locality')}))
#	culture=forms.CharField(widget=forms.Textarea(attrs={'placeholder':('list the culture you know in your locality')}))
#	class Meta:
#		model=Community
#		fields=('cuisines','arts','hotspots','culture',)				