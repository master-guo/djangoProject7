from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Stu
from django.urls import reverse

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!" + reverse("demo2",args=(100,"guo")))
    return HttpResponseRedirect(reverse("demo2",args=(10,"guo")))

def add(request):
    data = Stu.objects.get(id=2)
    print(data)
    return HttpResponse("add......")

# def demo_add(request):
#     return HttpResponse("demo_return")
#
# def demo_add1(request,sid):
#     return HttpResponse("demo_add1 and %d"%(sid))

def demo_add2(request,sid=0,name="",uid=""):
    return HttpResponse("demo_add2 and %d:%s:%s"%(sid,name,uid))

def fun(request,x,y):
    return HttpResponse("fun year:%s, month:%s"%(x,y))

def fun1(request,yy,mm):
    return HttpResponse("fun year:%s, month:%s"%(yy,mm))