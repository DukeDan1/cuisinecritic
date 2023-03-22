from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class Registration(forms.ModelForm):
	email = forms.EmailField(required=True)
	name = forms.CharField(required=True)
	avatar_src= forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		# additional fields to be displayed
		fields = ("email", "name", "avatar_src")
	
	def save(self, commit=True):
		user = super(Registration, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.avatar_src = self.cleaned_data['avatar_src']
		if commit:
			user.save()
		return user

