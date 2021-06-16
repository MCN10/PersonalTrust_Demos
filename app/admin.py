
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Beneficiary)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


class BeneficiaryAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated
    readonly_fields = ['author']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Beneficiary.customer = request.user.customer
        return super().get_form(request, obj, **kwargs)


    def save_model(self, request, obj, form, change):
        obj.customer = request.user.customer
        obj.author_id = request.user.id
        obj.save()
