from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def AuthPage(request):
    return render(request, 'auth_forms.html')