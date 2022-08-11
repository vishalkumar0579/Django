from django.shortcuts import render
from WebApp import  forms

# Create your views here.
def FeedbackView(request):
    form=forms.EmployeeFeedbackForms()
    MyDict={'form':form}
    return render(request,'WebApp/Templates/feedback_urls.html',MyDict)