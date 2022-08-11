from django.shortcuts import render

# Create your views here.
from Webapp.models import FilterModel

def DataView(request):
    datalist = FilterModel.objects.all()
    return render(request,'fiter.html',{'datas':datalist})