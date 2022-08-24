from django.shortcuts import render
from Webapp.models import Courses
from django.views.generic import ListView
# Create your views here.

class List_View_Data(ListView):
    template_name = 'model_data.html'
    context_object_name = 'courses'
    model = Courses

def Thanks(request):
    return render(request,'thanks.html')

