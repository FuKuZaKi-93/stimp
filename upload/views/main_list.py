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
from upload.models.rate import Rate
from upload.forms import (
    ImgForm,
)


from accounts.models import profile
from accounts.forms import (
    CustomUserCreationForm, SigninForm, ProfileForm
)




class ImgIndexView(generic.ListView):

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



        buisiness_scenes = buisiness_scene.BuisinessScene.objects.all()
        private_scenes = private_scene.PrivateScene.objects.all()
        seasons = season.Season.objects.all()
        colors = color.Color.objects.all()
        themes = theme.Theme.objects.all()

        context['buisiness_scenes'] = buisiness_scenes
        context['private_scenes'] = private_scenes
        context['seasons'] =seasons
        context['colors'] = colors
        context['themes'] = themes



        rate_img = Rate.objects.filter(user__exact=self.request.user,
                                       objent_id__exact=img.id)

        return context

    def get_queryset(self):
        # デフォルトは全件
        results = Img.objects.order_by('-favorited')

        # GETのURLクエリパラメータを取得する
        # 該当のクエリパラメータが存在しない場合は、[]が返ってくる
        q_buisiness_scenes = self.request.GET.getlist('buisiness_scene')
        q_private_scenes = self.request.GET.getlist('private_scene')
        q_seasons = self.request.GET.getlist('season')
        q_colors = self.request.GET.getlist('color')
        q_themes = self.request.GET.getlist('theme')

        if len(q_buisiness_scenes) != 0:
            buisiness_scenes = [x for x in q_buisiness_scenes]
            results = results.filter(buisiness_scene__in=buisiness_scenes)
        if len(q_private_scenes) != 0:
            private_scenes = [x for x in q_private_scenes]
            results = results.filter(private_scene__in=private_scenes)
        if len(q_seasons) != 0:
            seasons = [x for x in q_seasons]
            results = results.filter(season__in=seasons)
        if len(q_colors) != 0:
            colors = [x for x in q_colors]
            results = results.filter(color__in=colors)
        if len(q_themes) != 0:
            themes = [x for x in q_themes]
            results = results.filter(theme__in=themes)

        return results

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
