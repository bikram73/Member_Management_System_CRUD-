from django.shortcuts import redirect, render
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})


def add(request):
    return render(request,'add.html')

def addrec(request):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['email']
    d=request.POST['phonenumber']
    e=request.POST['country']
    mem=Member(firstname=a,lastname=b,email=c,phonenumber=d,country=e)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['email']
    d=request.POST['phonenumber']
    e=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=a
    mem.lastname=b
    mem.email=c
    mem.phonenumber=d
    mem.country=e
    mem.save()
    return redirect("/")