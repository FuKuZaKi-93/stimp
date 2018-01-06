from django.shortcuts import render, redirect
from upload.models import img, favorite


def favorite(request):
    if request.method == "POST":
        form = MyForm(data=request.POST) 
