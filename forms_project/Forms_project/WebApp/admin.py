from http import server
from django.contrib import admin
from WebApp.forms import EmployeeFeedbackForms

class ServiceFeedbackViewAdmin(admin.ModelAdmin):
    list_display = ('name_id','name','Phn_no','feedback','check')

admin.site.register(EmployeeFeedbackForms,ServiceFeedbackViewAdmin)
# Register your models here.
