from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  maha(request):
    return HttpResponse("<marquee><h1>hello hii friends</h1></marquee>")
def  lakshmi(request):
    return render(request,'app1_lucky.html')
