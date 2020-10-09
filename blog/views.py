from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request, 'first.html')

def academyfirst(request):
    return render(request, 'academyfirst.html')

def exhibition(request):
    return render(request, 'exhibition.html')

def login(request):
    return render(request, 'login.html')

def studentforth(request):
    return render(request, 'studentforth.html')

def studentsecond(request):
    return render(request, 'studentsecond.html')

def studentthird(request):
    return render(request, 'studentthird.html')
