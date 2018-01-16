from django.shortcuts import render, redirect
from upload.models import img, favorite
from django.http import JsonResponse


def favorite(request):
    if request.method == 'POST':
        user = request.user
        img_pk = request.POST.get('num')
        obj = img.Img.objects.get(pk=img_pk)

        if favorite.Favorite.objects.filter(user=user,content_object=obj).exists():
            
        else:
            favo = favorite.Favorite.objects.create(user=user,content_object=obj)
            favo.save()
            return JsonResponse()
