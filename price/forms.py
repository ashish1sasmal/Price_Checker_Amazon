from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['email','password1','password2']


	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget = forms.EmailInput(attrs={'class': 'fadeIn second', 'placeholder': 'Email Address '})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Enter Password '})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'fadeIn fourth', 'placeholder': 'Password confirmation'})

class ProfileForm(forms.ModelForm):
	mobile=forms.CharField()
	class Meta():
		model = Profile
		fields=('mobile',)

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['mobile'].widget = forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': 'Enter phone Number '})
