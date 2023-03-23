from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Restaurant

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

CATEGORY_CHOICES= [
    ('mexican', 'Mexican'),
    ('chinese', 'Chinese'),
    ('thai', 'Thai'),
    ('indian', 'Indian'),
    ]

class CreateResturaunt(forms.ModelForm):
	name=forms.CharField(required=True)
	address=forms.CharField(required=True)
	category=forms.CharField(label="Select...", widget=forms.Select(choices=CATEGORY_CHOICES))
	slug=forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Restaurant
		fields = ("name", "address", "category")

	def save(self, commit=True):
		resturaunt = super(CreateResturaunt, self).save(commit=False)
		resturaunt.name = self.cleaned_data["name"]
		resturaunt.address = self.cleaned_data["address"]
		resturaunt.category = self.cleaned_data["category"]
		if commit:
			resturaunt.save()
		return resturaunt