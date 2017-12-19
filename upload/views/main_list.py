from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count


from upload.models import (
    img,
    situation, color, member, season, place,
)
from upload.forms import (
    ImgForm,
    SituationForm, ColorForm, MemberForm, SeasonForm, PlaceForm,
)


from accounts.models import profile
from accounts.forms import (
    CustomUserCreationForm, SigninForm, ProfileForm
)


class ImgIndexView(generic.ListView):
    def get_queryset(self):
        return img.Img.objects.order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['situation_list'] = situation.Situation.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
#        context['whowith_list'] = whowith.WhoWith.objects.annotate(
#            img_num=Count('img')).order_by('-img_num')[:3]
        context['color_list'] = color.Color.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['member_list'] = member.Member.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['season_list'] = season.Season.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]
        context['place_list'] = place.Place.objects.annotate(
            img_num=Count('img')).order_by('-img_num')[:3]

        return context
    paginate_by = 30
    template_name = 'upload/main_list.html'
