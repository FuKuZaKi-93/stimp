from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count


from upload.models import (
    buisiness_scene, private_scene, color, season, theme,
)
from upload.models.img import Img
from upload.models.like import Like
from upload.forms import (
    ImgForm,
)


from accounts.models import profile
from accounts.forms import (
    CustomUserCreationForm, SigninForm, ProfileForm
)




class ImgIndexView(generic.ListView):
    def get_queryset(self):
        return Img.objects.order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['buisiness_scene_list'] = buisiness_scene.BuisinessScene.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['private_scene_list'] = private_scene.PrivateScene.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['color_list'] = color.Color.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['season_list'] = season.Season.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['theme_list'] = theme.Theme.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]

        context['like_counter'] = Like.objects.annotate(like_num=Count('object_id'))

        return context
    paginate_by = 30
    template_name = 'upload/main_list.html'


"""
def for_ajax(req):    # AJAXに答える関数
    import json
    from django.http import HttpResponse,Http404

    if req.method == 'POST':
        txt = req.POST['your_txt']  # POSTデータを取得して
        surprise_txt = txt + "!!!"  # 加工
        
        response = json.dumps({'':,})  # JSON形式に直して・・

        return HttpResponse(response,mimetype="text/javascript")  # 返す。JSONはjavascript扱いなのか・・

    else:
        raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも
"""
