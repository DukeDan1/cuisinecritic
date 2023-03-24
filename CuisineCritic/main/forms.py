from django import forms
from .models import Category, UserProfile, Restaurant

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


def get_category_choices():
	categories = Category.objects.all()
	category_choices = []
	for x in categories:
		category_choices.append((x.category_id, x.name))
	return category_choices


class CreateRestaurant(forms.ModelForm):
	name=forms.CharField(required=True)
	address=forms.CharField(required=True)
	category=forms.CharField(label="Select...", widget=forms.Select(choices=get_category_choices()))
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