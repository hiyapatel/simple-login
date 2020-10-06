from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Emp
#from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .serializers import EmpSerializer

def login(request):
    return render(request,"../templates/login.html")

def signup(request):
    return render(request,"../templates/signup.html")

def new_user(request):
    v1 = request.GET['t1']
    v2 = request.GET['t2']
    v3 = request.GET['t3']
    v4 = request.GET['t4']

    Emp.objects.create(ename=v1,epass=v2, eemail=v3, eage=v4)
    return render(request,"../templates/done.html")

def login_info(request):
    v1 = request.GET['t1']
    v2 = request.GET['t2']
    try:
        e = Emp.objects.get(ename=v1,epass=v2)
        dict = {"name":e[0]}
        return render(request,"../templates/found.html",dict)
    except:
        return render(request,"../templates/again.html")
