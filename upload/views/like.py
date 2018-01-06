from django.shortcuts import render, redirect
from upload.models import img
from upload.models.like import Like
from django.http import JsonResponse



def like(request, id):
    user = request.user
    obj  = img.Img.objects.get(id=id)
    if request.method == 'POST':
        like = Like.objects.create(user=user,content_object=obj)
        like.save()
        return JsonResponse()

"""
def like(request, id):
    user = request.user
    obj  = img.Img.objects.get(id=id)
    if request.method == 'POST':
        like = Like.objects.create(user=user,content_object=obj)
        like.save()
        return redirect('upload:main_list')
"""
