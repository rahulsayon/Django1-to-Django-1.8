from django.shortcuts import render
from django.utils.translation import gettext 
import datetime

def PostView(request):
    context =  {}
    context["title"] = "rahul"
    context['date'] = datetime.datetime.now()
    context['list'] =  [ 'Rahul' , 'Sonu' , 'Ravi' ]
    return render(request,"home.html", context)