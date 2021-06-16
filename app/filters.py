import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']

class BeneficiaryFilter(django_filters.FilterSet):
	class Meta:
		model = Beneficiary
		fields = ['name', 'email']

class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = Category
		fields = ['category_name']
