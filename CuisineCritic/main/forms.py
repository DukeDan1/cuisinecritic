from django import forms
from .models import Category, UserProfile, Restaurant, RestaurantImage

class Registration(forms.ModelForm):
	# email = forms.EmailField(required=True)
	# name = forms.CharField(required=True)
	# avatar_src= forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		fields = ("email", "name", "avatar_src")
	
	def save(self, commit=True):
		user = super(Registration, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.avatar_src = self.cleaned_data['avatar_src']
		if commit:
			user.save()
		return user






class CreateRestaurant(forms.ModelForm):

	class Meta:
		model = Restaurant
		fields = ("name", "address", "category")

	def save(self, commit=True):
		restaurant = super(CreateRestaurant, self).save(commit=False)
		restaurant.name = self.cleaned_data["name"]
		restaurant.address = self.cleaned_data["address"]
		restaurant.category = self.cleaned_data["category"]
		

		if commit:
			restaurant.save()
		return restaurant