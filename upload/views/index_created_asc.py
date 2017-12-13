from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count

from upload.models import (
    Img,
    Situation, ClothColor, CoordinateStyle, Season, Purpose,
    Comment,
)
from upload.forms import (
    ImgForm,
    SituationForm, ColorForm, StyleForm, SeasonForm, PurposeForm,
    CommentCreateForm,
)




class ImgIndexView(generic.ListView):
#    model = Img
    def get_queryset(self):
        results = Img.objects.order_by('-created_at')


        q_sort = self.request.GET.get('sort')

        if q_sort is not None:
            results = results.order_by(q_sort)


        return results
#        try:
#            select = request.POST['sortselect']
#            if select == "asc":
#                select = "created_at"
#                return selected
#            elif select == "desc":
#                select = "-created_at"
#                return selected
#            elif select == "popular":
#                select = "created_at"
#                return selected
#            elif select == "many":
#                select = "-created_at"
#                return selected
#        except:
#            select = "created_at"
#            return selected
#        return Img.objects.order_by('-created_at')

#        if self.request.method == 'POST':
#            return Img.objects.order_by(
#                str(self.request.POST['sortselect']))
#        else:
#            return Img.objects.order_by('created_at')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['situation_list'] = Situation.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['color_list'] = ClothColor.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['style_list'] = CoordinateStyle.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['season_list'] = Season.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['purpose_list'] = Purpose.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        return context
    paginate_by = 30
    template_name = 'upload/index_created_asc.html'
