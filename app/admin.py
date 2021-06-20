
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Owner)
admin.site.register(Task)



class TaskAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated
    readonly_fields = ['owner']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Task.owner = request.user.owner
        return super().get_form(request, obj, **kwargs)


    def save_model(self, request, obj, form, change):
        obj.owner = request.user.owner
        obj.save()
