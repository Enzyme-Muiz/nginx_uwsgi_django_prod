from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    #return HttpResponse("I love <strong> my </strong> wife")
    return render(request, 'html_only/home.html')
