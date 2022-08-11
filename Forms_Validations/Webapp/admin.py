from django.contrib import admin
from Webapp.models import FormValidations

# Register your models here.

class ValidationModelAdmin(admin.ModelAdmin):
    list_display = ['name_id','name','Phn_no','feedback']
admin.site.register(FormValidations,ValidationModelAdmin)