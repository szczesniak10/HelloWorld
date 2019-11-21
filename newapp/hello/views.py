from django.shortcuts import render, HttpResponse
from django.http import  HttpResponse
from django.http import JsonResponse

# Create your views here.
def myView(request):
    return  render(request,'newapp/sample.html')

def index(request):
    comments=[
    {"Message":"Hello World!"}
    ]
    return JsonResponse({'comments': comments})
