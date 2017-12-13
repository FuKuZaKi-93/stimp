from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import CustomUserCreationForm, SigninForm

@login_required
def index(request):
    return render(request, 'main/index.html')

def signup(request):
    form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form,})

def create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stimp/top/')
        return render(request, 'accounts/signup.html', {'form': form,})
    else:
        raise Http404

def signin(request):
    form = SigninForm()
    return render(request, 'accounts/signin.html', {'form': form,})

