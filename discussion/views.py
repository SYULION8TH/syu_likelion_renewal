from django.shortcuts import render 
from django.http import JsonResponse
from main import models

# Create your views here.

def home(request):
   # return render(request, "./ ")
   return JsonResponse({"key" : "Hello" })

