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





class CreateResturaunt(forms.ModelForm):
	# name=forms.CharField(required=True)
	# address=forms.CharField(required=True)
	
	# categories = Category.objects.all()
	# category_choices = []
	# for x in categories:
	# 	category_choices.append((x.category_id, x.name))

	#category=forms.CharField(label="Select...", widget=forms.Select(choices=categories))
	# slug is created automatically

	class Meta:
		model = Restaurant
		fields = ("name", "address", "category")

	def save(self, commit=True):
		resturaunt = super(CreateResturaunt, self).save(commit=False)
		resturaunt.name = self.cleaned_data["name"]
		resturaunt.address = self.cleaned_data["address"]
		category = self.cleaned_data["category"]

		try:
			resturaunt.category = Category.objects.get(category_id=category)
		except Category.DoesNotExist:
			raise forms.ValidationError("Category does not exist")
		

		if commit:
			resturaunt.save()
		return resturaunt