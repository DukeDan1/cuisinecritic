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





<<<<<<< HEAD
class CreateRestaurant(forms.ModelForm):
	name=forms.CharField(required=True)
	address=forms.CharField(required=True)
	category=forms.CharField(label="Select...", widget=forms.Select(choices=get_category_choices()))
=======
class CreateResturaunt(forms.ModelForm):
	# name=forms.CharField(required=True)
	# address=forms.CharField(required=True)
	
	# categories = Category.objects.all()
	# category_choices = []
	# for x in categories:
	# 	category_choices.append((x.category_id, x.name))

	#category=forms.CharField(label="Select...", widget=forms.Select(choices=categories))
>>>>>>> a3ba9762eee4f864bb30d6f7dd701a5434582990
	# slug is created automatically

	class Meta:
		model = Restaurant
		fields = ("name", "address", "category")

	def save(self, commit=True):
		restaurant = super(CreateRestaurant, self).save(commit=False)
		restaurant.name = self.cleaned_data["name"]
		restaurant.address = self.cleaned_data["address"]
		category = self.cleaned_data["category"]

		try:
			restaurant.category = Category.objects.get(category_id=category)
		except Category.DoesNotExist:
			raise forms.ValidationError("Category does not exist")
		

		if commit:
			restaurant.save()
		return restaurant