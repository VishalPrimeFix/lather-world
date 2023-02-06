from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from project import models as project_models
from myadmin import models as myadmin_models
from django.conf import settings
import time
MEDIA_URL = settings.MEDIA_URL

def sessioncheckuser_middleware(get_response):
    def middleware(request):
        if request.path=='/user/':
            if request.session['sunm']==None or request.session['srole']!='user':
                response = redirect('/login/')
            else:
                response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware

# Create your views here.

def userhome(request):
    return render(request,'userhome.html',{'sunm': request.session['sunm']})

def funds(request):
    paypalURL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
    paypalID = 'sb-njixz18057931@business.example.com'
    # personalID = 'sb-xgzi318692648@personal.example.com' password = QO0VEab<
    price = 100
    return render(request,'funds.html',{'sunm': request.session['sunm'],'paypalURL':paypalURL, 'paypalID':paypalID, 'price':price})

def payment(request):
    sunm=request.GET.get('sunm')
    price=request.GET.get('price')
    info = time.asctime()
    p=models.Payment(uid=sunm,price=price,info=info)
    p.save()
    return redirect('/user/success/')

def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')

def paymentdetails(request):
    paymentinfo = models.Payment.objects.filter(uid=request.session['sunm'])
    return render(request,'paymentdetails.html',{'paymentinfo':paymentinfo,'sunm':request.session['sunm']})

def cpuser(request):
    sunm = request.session['sunm']
    if request.method=='GET':
        return render(request,'cpuser.html')
    else:
        opass = request.POST.get('opass')
        npass = request.POST.get('npass')
        cnpass = request.POST.get('cnpass')
        userDetails = project_models.Register.objects.filter(username=sunm,password=opass)
        if len(userDetails)>0:
            if npass==cnpass:
                project_models.Register.objects.filter(username=sunm,password=opass).update(password=npass)
                msg = 'Password Changed Successfully'
            else:
                msg = "New And Confirm New Password Not Matches!!!"
        else:
            msg = 'Invalid Old Password!!! Please try again'
        
        return render(request,"cpuser.html",{"sunm":sunm,"msg":msg})

def epuser(request):
    sunm = request.session['sunm']
    userDetails = project_models.Register.objects.filter(username=sunm)
    m,f = '',''
    if userDetails[0].gender=='male':
        m = 'checked'
    else:
        f='checked'
    if request.method=='GET':
        return render(request,"epuser.html",{"sunm":sunm,'userDetails':userDetails[0],"m":m,"f":f,'output':''})
    else:
        name = request.POST.get("name")
        username = request.POST.get("username")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        p = project_models.Register.objects.filter(username=sunm).update(username=username,name=name,address=address,mobile=mobile,city=city,gender=gender)
        return render(request,"epuser.html",{"sunm":sunm,'userDetails':userDetails[0],"m":m,"f":f,'output':'Edit successfully'})

def showcategory(request):
    sunm = request.session['sunm']
    clist=myadmin_models.category.objects.all()
    return render(request,'showcategory.html',{'sunm':sunm,'clist':clist,'MEDIA_URL':MEDIA_URL})

def showsubcategory(request):
    sunm = request.session['sunm']
    clist=myadmin_models.category.objects.all()
    catnm = request.GET.get('catnm')
    sclist=myadmin_models.subcategory.objects.filter(catnm=catnm)
    return render(request,'showsubcategory.html',{'sunm':sunm,'catnm':catnm,'sclist':sclist,'clist':clist,'MEDIA_URL':MEDIA_URL})

def showproduct(request):
    catnm = request.GET.get('catnm')
    subcatnm = request.GET.get('subcatnm')
    sunm = request.session['sunm']
    sclist=myadmin_models.subcategory.objects.filter(catnm=catnm)
    plist=myadmin_models.Product.objects.filter(psubcategory=subcatnm)
    return render(request,'showproduct.html',{'sunm':sunm,'MEDIA_URL':MEDIA_URL,'sclist':sclist,'plist':plist,'catnm':catnm,'subcatnm':subcatnm})

def order(request):
    qty = request.POST.get('qty')
    pprice = request.POST.get('pprice')
    amount = int(qty)*int(pprice)
    pid = request.POST.get('pid')
    uid = request.session['sunm']
    info = time.asctime()
    p=models.Order(pid=int(pid),amount=amount,qty=int(qty),pprice=pprice,uid=uid,info=info)
    p.save()
    return render(request,"order.html",{"sunm":request.session['sunm']})