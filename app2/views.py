from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def narsi(request):
    return HttpResponse("hii thammudu hello")
def shanti(request):
    return render(request,'app2_lucky.html')