from django.http import HttpResponse,request
from django.shortcuts import render
from service.models import service
from contact.models import contactEnquiry


def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('phone')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        en=contactEnquiry(name=name,email=email,phone=phone,message=message)
        en.save()
    
    return render(request,"index.html")

def Homepage(request):
    serviceData=service.objects.all()
    data={
        'serviceData':serviceData
    }
    return render(request,"index.html",data)