from django.shortcuts import render,HttpResponseRedirect, redirect
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def index(request):
    return render(request, 'index.html', {})


def logoutUser(request):
    logout(request)
    return redirect("index")
