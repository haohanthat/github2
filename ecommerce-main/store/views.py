from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
# Create your views here.
def store(request):
    return render(request, 'store.html',{})
    

def register(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form':form})

def login(request):
    form=login()
    if request.method=="login":
        form=RegistrationForm(request.login)
    return render(request, 'login.html', {'form':form})