from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin
from upload.models import (
    img,
)
from upload.forms import (
    ImgForm,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Count

#from extra_views import CreateWithInlinesView, InlineFormSet


class ImgMyListView(generic.ListView):
    def get_queryset(self):
        return img.Img.objects.filter(user__exact=self.request.user).order_by('-created_at')
    paginate_by = 30


class ImgCreateUserView(generic.CreateView):
    model = img.Img
    form_class = ImgForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(ImgCreateUserView, self).form_valid(form)

    success_url = reverse_lazy("upload:main_list")


class ImgUpdateView(generic.UpdateView):
    model = img.Img
    form_class = ImgForm
    success_url = reverse_lazy("upload:mypage")
 
 
class ImgDeleteView(generic.DeleteView):
    model = img.Img
    success_url = reverse_lazy("upload:mypage")




"""    def get_context_data(self, **kwargs):
        context = super(ImgDetailView, self).get_context_data(**kwargs)
        return context
"""


class ImgDetailWithCommentView(generic.DetailView):
    model = img.Img
    """
    form_class = CommentCreateForm
    def form_valid(self, form):
        img_pk = self.kwargs['pk']
        self.object = form.save(commit=False)
        self.object.target = img.Img.objects.get(pk=img_pk)
        self.object.save()
        return redirect('upload:detail', pk=img_pk)

    def img(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    """

class ImgVoteView(generic.UpdateView):
    model = img.Img
    form_class = ImgForm
    success_url = reverse_lazy("upload:mypage")

