from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
def first(request):
    return render(request, 'first.html')

#@login_required
def academyfirst(request):
    return render(request, 'academyfirst.html')

#@login_required
def exhibition(request):
    return render(request, 'exhibition.html')

def logintest(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    if username == "aaa" and password == "123":
        return HttpResponseRedirect("/first/")
    else:
        return HttpResponse("login fail")

def login(request):
    return render(request, 'login.html')

#@login_required
def studentforth(request):
    return render(request, 'studentforth.html')

#@login_required
def studentsecond(request):
    return render(request, 'studentsecond.html')

#@login_required
def studentthird(request):
    return render(request, 'studentthird.html')

#@login_required
def video(request):
    return render(request, 'video.html')

#@login_required
def examination(request):
    return render(request, 'examination.html')

#@login_required
def xueyuan2(request):
    return render(request, 'xueyuan2.html')


#@login_required
def material(request):
    return render(request, 'material.html')

#@login_required
def feedback(request):
    return render(request, 'feedback.html')