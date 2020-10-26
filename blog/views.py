from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def first(request):
    return render(request, 'first.html')

def academyfirst(request):
    return render(request, 'academyfirst.html')

def exhibition(request):
    return render(request, 'exhibition.html')

def logintest(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    if username == "aaa" and password == "123":
        return redirect("http://localhost:8000")
    else:
        return HttpResponse("login fail")

def login(request):
    return render(request, 'login.html')

def studentforth(request):
    return render(request, 'studentforth.html')

def studentsecond(request):
    return render(request, 'studentsecond.html')

def studentthird(request):
    return render(request, 'studentthird.html')

def video(request):
    return render(request, 'video.html')