from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contactus
from django.contrib import messages

def index(request):
    context={
        "variable":"This is variable"
    }
    return render(request,'index.html',context) 
def about(request):
    return render(request,'about.html')

def contactus(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        description=request.POST.get('description')
        contactus=Contactus(first_name=first_name,last_name=last_name, email=email,phone=phone,description=description,date=datetime.today())
        contactus.save()
        messages.success(request, "Your message has been send!")
    return render(request,'contactus.html')