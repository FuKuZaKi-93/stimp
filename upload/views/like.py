from django.shortcuts import render, redirect
from upload.models.img import Img
from upload.models.like import Like
from django.http import JsonResponse
from django.http import HttpResponse
import json


def like(request,id):
    if request.method == 'POST':
        user = request.user
        obj  = Img.objects.get(id=id)
        like = Like.objects.create(user=user,content_object=obj)
        like.save()

        obj.favorited += 1
        obj.save()
        #data = request.POST.get('id')
        ok = "お気に入りに登録しました。"
        #response = json.dumps({'message':request.POST.get('id')})
        #return HttpResponse(response)

        d = {
            'message': ok
        }
        return JsonResponse(d)

"""
def like(request, id):
    user = request.user
    obj  = img.Img.objects.get(id=id)
    if request.method == 'POST':
        like = Like.objects.create(user=user,content_object=obj)
        like.save()
        return redirect('upload:main_list')
"""
