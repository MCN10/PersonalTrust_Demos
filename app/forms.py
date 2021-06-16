from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = OrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = ShippingAddress
		fields = '__all__'


class BeneficiaryForm(ModelForm):
    class Meta:
        model = Beneficiary
        fields = '__all__'
        readonly_fields = 'customer'


class CategoriesForm(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		exclude = ['slug']