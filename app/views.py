from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test(request):
    return HttpResponse("yessss")

def testtemplate(request):
    return render(request,"hello.html")

def Welcome(request):
    return render(request,"welcome.html")
