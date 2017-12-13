from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Theme
from .forms import ThemeForm

from django.views import generic


class ThemeListView(generic.ListView):
    def get_queryset(self):
        return Theme.objects.order_by('-created_at')
    pagenated_by = 5 
#    template_name = 'base.html'


class ThemeCreateView(generic.CreateView):
    model = Theme
    form_class = ThemeForm
    template_name = 'categories/create_theme.html'
    success_url = reverse_lazy("categories:create_theme")
"""
    def form_valid(self, form):
        if form.is_valid():
            instance = form.sava(commit=False)
            instance.user = self.request.user
            instance.save()
        else:
"""
            
"""
def createTheme(request):
    if requst.method == 'POST':
        model = Theme()
        form = ThemeForm(request.POST, instance=model)
        if form.is_valid():
            t = form.commit=False)
            t.sava()
        return render('categories/create.html', dict(form=form, 
"""
