from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home.html')

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1+val2
    return render(request,'result.html',{'result':res})

def sub(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1-val2
    return render(request,'result.html',{'result':res})

def mul(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1*val2
    return render(request,'result.html',{'result':res})

def div(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    if val2 != 0:
        res = val1/val2
        return render(request,'result.html',{'result':res})
    else:
        return HttpResponse("Division by zero is not possible")
    