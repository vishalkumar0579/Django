from django.contrib import admin
from Webapp.models import Courses
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    lsit_display = ['Name', 'Trainer', 'Location', 'Days']
admin.site.register(Courses, CourseAdmin)