from django.shortcuts import redirect, render
from project import models as myproject_models
from django.core.files.storage import FileSystemStorage
from project import models as project_models
from django.http import HttpResponse
from . import models
import time
#middleware to check session for admin routes
def sessioncheckmyadmin_middleware(get_response):
    def middleware(request):
        if request.path=='/myadmin/' or request.path=='/myadmin/addcategory/' or request.path=='/myadmin/addsubcategory/' or request.path=='/myadmin/manageusers' or request.path=='/myadmin/manageuserstatus':
            if request.session['sunm']==None or request.session['srole']!='admin':
                response = redirect('/login/')
            else:
                response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware
# Create your views here.

def adminhome(request):
    return render(request,"adminhome.html",{"sunm": request.session['sunm']})

def manageusers(request):
    userDetails=myproject_models.Register.objects.filter(role="user")
    return render(request,"manageusers.html",{"userDetails":userDetails})

def manageuserstatus(request):
    status=request.GET.get("status")    
    regid=request.GET.get("regid") 
    if status=="block":
        myproject_models.Register.objects.filter(regid=int(regid)).update(status=0)
    elif status=="verify":
        myproject_models.Register.objects.filter(regid=int(regid)).update(status=1)
    else:
        myproject_models.Register.objects.filter(regid=int(regid)).delete()

    return redirect("/myadmin/manageusers/")

def addcategory(request):
    if request.method=="GET":
        return render(request,'addcategory.html',{"output": ""})
    else:
        catnm = request.POST.get('catnm')
        caticon = request.FILES['caticon']
        fs = FileSystemStorage()
        filename = fs.save(caticon.name,caticon)
        p = models.category(catnm=catnm,caticonnm=filename)
        p.save()        
        return render(request,'addcategory.html',{"output": "Category Added"})


def addsubcategory(request):
    clist = models.category.objects.all()
    if request.method=="GET":
        return render(request,'addsubcategory.html',{"clist":clist,"output": ""})
    else:
        catnm = request.POST.get('catnm')
        subcatnm = request.POST.get('subcatnm')
        caticon = request.FILES['caticon']
        fs = FileSystemStorage()
        filename = fs.save(caticon.name,caticon)
        p = models.subcategory(catnm=catnm,subcatnm=subcatnm,subcaticonnm=filename)
        p.save()        
        return render(request,'addsubcategory.html',{"clist":clist,"output": "Category Added"})

def cpadmin(request):
    sunm = request.session['sunm']
    if request.method=='GET':
        return render(request,'cpadmin.html')
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
        
        return render(request,"cpadmin.html",{"sunm":sunm,"msg":msg})

def epadmin(request):
    sunm = request.session['sunm']
    userDetails = project_models.Register.objects.filter(username=sunm)
    m,f = '',''
    if userDetails[0].gender=='male':
        m = 'checked'
    else:
        f='checked'
    if request.method=='GET':
        return render(request,"epadmin.html",{"sunm":sunm,'userDetails':userDetails[0],"m":m,"f":f,'output':''})
    else:
        name = request.POST.get("name")
        username = request.POST.get("username")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        p = project_models.Register.objects.filter(username=sunm).update(username=username,name=name,address=address,mobile=mobile,city=city,gender=gender)
        return render(request,"epadmin.html",{"sunm":sunm,'userDetails':userDetails[0],"m":m,"f":f,'output':'Edit successfully'})

def addproduct(request):
    sunm = request.session['sunm']
    clist = models.category.objects.all()
    sclist = models.subcategory.objects.all()
    if request.method=='GET':
        return render(request,'addproduct.html',{'sunm':sunm,'clist':clist,'sclist':sclist,'output':''})
    else:
        ptitle = request.POST.get('ptitle')
        pcategory = request.POST.get('pcategory')
        psubcategory = request.POST.get('psubcategory')
        pdescription = request.POST.get('pdescription')
        pprice = request.POST.get('pprice')
        info = time.asctime()
        picon = request.FILES['picon']
        fs = FileSystemStorage()
        filename = fs.save(picon.name,picon)
        p=models.Product(ptitle=ptitle,pcategory=pcategory,piconnm=filename,psubcategory=psubcategory,pdescription=pdescription,pprice=pprice,uid=sunm,info=info)
        p.save()
        return render(request,'addproduct.html',{'sunm':sunm,'clist':clist,'sclist':sclist,'output':'Product Added Successfully ....'})
        

def scAJAX(request):
    catnm = request.GET.get("catnm")
    sclist=models.subcategory.objects.filter(catnm=catnm)
    sclist_options="<option>Select Sub-Category</option>"
    for row in sclist:
        sclist_options+=("<option>"+row.subcatnm+"</option>")
    return HttpResponse(sclist_options)