from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')
@login_required
def AuthPage(request):
    return render(request, 'auth_forms.html')

def LogOut(request):
    return render(request, 'registration/logout.html')