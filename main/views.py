from django.shortcuts import render
from . import models
from .models import *

# Create your views here.

def base(request):
    return render(request, "html/base.html")

def member_view(request):
    members = member.objects.all()
    return render(request, "html/base.html")

def intro(request):
    return render(request, "html/intro.html")
