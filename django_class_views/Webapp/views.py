import imp
from django.shortcuts import render
from django.views.generic import View , TemplateView
# Create your views here.

from django.http import HttpResponse

class MyClass(View):
    def get(self, request):
        return HttpResponse("Welcome to Class Based Views...!")
    
    def post(self, request):
        return HttpResponse("Post Method called...!")

class TempView(View):
    def get(self, request):
        return HttpResponse("<h1>Welcome to Class Based Views...!</h1>")
        # return render(request, 'tempview.html')

class TempCBV(TemplateView):
    template_name = 'tempview.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['EmpName'] = 'Vishal'
        context['EmpLocation'] = 'Odisha'
        context['EmpAddress'] = 'Bbsr'
        return context

