from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count

from extra_views import CreateWithInlinesView, InlineFormSet


"""
class ImgIndexView(generic.ListView):
    def get_queryset(self):
        return Img.objects.order_by('-created_at')

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
    template_name = 'upload/index.html'
"""


class ImgMyListView(generic.ListView):
    def get_queryset(self):
        return Img.objects.filter(user__exact=self.request.user).order_by('-created_at')
    paginate_by = 30


class ImgCreateUserView(generic.CreateView):
    model = Img
    form_class = ImgForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(ImgCreateUserView, self).form_valid(form)

    success_url = reverse_lazy("upload:index")


class ImgUpdateView(generic.UpdateView):
    model = Img
    form_class = ImgForm
    success_url = reverse_lazy("upload:mypage")
 
 
class ImgDeleteView(generic.DeleteView):
    model = Img
    success_url = reverse_lazy("upload:mypage")


class ImgEvent01View(generic.ListView):
    queryset = Img.objects.filter(category__exact=u"後期中間発表で着る服").order_by('-created_at')
    paginate_by = 6
    template_name = 'upload/event01.html'


"""    def get_context_data(self, **kwargs):
        context = super(ImgDetailView, self).get_context_data(**kwargs)
        return context
"""


class ImgDetailWithCommentView(FormMixin, generic.DetailView):
    model = Img
    form_class = CommentCreateForm
    def form_valid(self, form):
        img_pk = self.kwargs['pk']
        self.object = form.save(commit=False)
        self.object.target = Img.objects.get(pk=img_pk)
        self.object.save()
        return redirect('upload:detail', pk=img_pk)

    def img(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ImgVoteView(generic.UpdateView):
    model = Img
    form_class = ImgForm
    success_url = reverse_lazy("upload:mypage")


class SituationCreate(generic.CreateView):
    model = Situation
    form_class = SituationForm
    template_name = 'upload/situation_create.html'
    success_url = reverse_lazy("upload:create")
