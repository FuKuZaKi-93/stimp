from django.views import generic
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count

from upload.models import Img
from upload.forms import ImgForm


@require_POST
def sort(request):
    model = Img

    select = request.POST['selectsort']
    
