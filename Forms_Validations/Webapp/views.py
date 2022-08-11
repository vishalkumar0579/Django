from django.shortcuts import render
from Webapp import forms
from django.http import HttpResponseRedirect
from Webapp.models import FormValidations


# Create your views here.
def ThankView(request):
    return render(request,'thanks.html')

def ByeView(request):
    return render(request,'bye.html')

def FormValidationViews(request):
    if request.method=='POST':
        print("if ------",request,"-------method---------",request.method)
        # form=forms.validation(request.POST)
        form=forms.validationLimit(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
        else:
            return HttpResponseRedirect('/bye')

    else:
        print("else",request,"-------method---------",request.method)
        # form=forms.validation()
        form=forms.validationLimit()
    return render(request,'validation_form.html',{'form':form})

def ShowData(request):
    model=FormValidations.objects.all()
    return render(request,'show_data.html',{'all_data':model})