from django.shortcuts import render

# Create your views here.
def webpage1(request):
    return render(request,'webpage1.html')
def webpage2(request):
    return render(request,'webpage2.html')