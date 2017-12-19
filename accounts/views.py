from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, SigninForm, ProfileForm


@login_required
def index(request):
    return render(request, 'main/index.html')


def signup(request):
 
    user_form = CustomUserCreationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
 
        # Userモデルの処理。ログインできるようis_staffをTrueにし保存
        user = user_form.save(commit=False)
        user.is_staff = True
        user.save()
 
        # Profileモデルの処理。↑のUserモデルと紐づけましょう。
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
 
        login(
            request, user, backend="django.contrib.auth.backends.ModelBackend")
 
        return redirect("/stimp/top/")
 
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, 'accounts/signup.html', context)

"""
    user_form = CustomUserCreationForm()
    profile_form = ProfileForm()
    return render(request, 'accounts/signup.html',
                  {'user_form': user_form,
                   'prfile_form': profile_form,})
"""

def create(request):
 
    user_form = CustomUserCreationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
 
        # Userモデルの処理。ログインできるようis_staffをTrueにし保存
        user = user_form.save(commit=False)
        user.is_staff = True
        user.save()
 
        # Profileモデルの処理。↑のUserモデルと紐づけましょう。
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
 
        login(
            request, user, backend="django.contrib.auth.backends.ModelBackend")
 
        return redirect("/stimp/top/")
 
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, 'accounts/signup.html', context)

"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stimp/top/')
        return render(request, 'accounts/signup.html', {'form': form,})
    else:
        raise Http404
"""


def signin(request):
    form = SigninForm()
    return render(request, 'accounts/signin.html', {'form': form,})

