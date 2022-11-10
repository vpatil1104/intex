from re import template
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")
  

def home(request):
      return HttpResponse("This is my home page")

def newline(request):
    return HttpResponse("this is newline vivek")

def contact(request):
      if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            desc=request.POST.get('desc')
            contact=contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
            contact.save()
            return render(request,'contact-us.html')
        #return HttpResponse("this is contact page")