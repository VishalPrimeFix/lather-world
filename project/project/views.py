from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
import time

def sessioncheck_middleware(get_response):
    def middleware(request):
        if request.path=='/home/' or request.path=='/about/' or request.path=='/login/' or request.path=='register' or request.path=='service' or request.path=='/contact/':
            request.session['sunm']=None
            request.session['srole']=None
            response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")


def register(request):
    if request.method=="GET":
        return render(request,"register.html")
    else:
        #receive data on UI
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        dt = time.asctime()

        p = models.Register(name=name,username=username,password=password,address=address,mobile=mobile,city=city,gender=gender,status=0,role="user",dt=dt)
        p.save()
        return render(request,"register.html",{"output":"user register successfully!!"})

def login(request):
    if request.method=="GET":
      return render(request,"login.html",{"output":""})
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        # models.Register.objects.all() # fetch all the contentfrom orm table
        userDetails=models.Register.objects.filter(username=username,password=password,status=1)
        # print(userDetails)
        if len(userDetails)>0:

            # To store data in session storage
            request.session['sunm']=userDetails[0].username
            request.session['srole']=userDetails[0].role

            if userDetails[0].role == "admin":
              return redirect("/myadmin/")  
            else:
              return redirect("/user/")   
        else:
            return render(request,"login.html",{"output":"invalid login !!!"})


def ajaxResponse(request):
    return HttpResponse('AJAX code Working !!!')

def checkUsername(request):
    username = request.GET.get('username')
    result = models.Register.objects.filter(username__contains = username)
    if len(result)>0:
        return HttpResponse(1)
    else:
        return HttpResponse(0)