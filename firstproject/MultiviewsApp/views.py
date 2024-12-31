from django.shortcuts import render;
from django.http import HttpResponse;

# Create your views here.
   
def f111(request): 
	return HttpResponse("<h2>Good Morning User..!! Have a Nice day...</h2><hr/>");

def f222(request): 
	return HttpResponse("<h2>Good Afternoon User..!! Hope you are doing good...</h2><hr/>");

def f333(request): 
	return HttpResponse("<h2>Good Evening User..!! How was ur day...</h2><hr/>"); 
