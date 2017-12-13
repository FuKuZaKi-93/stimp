from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^SignUp$', views.signup, name='signup'),
    url(r'^create$', views.create, name='create'),
    url(r'^SignIn$', auth_views.login, {'template_name': 'accounts/signin.html'}, name='signin'),
    url(r'^SignOut$', auth_views.logout, name='signout'),
]
