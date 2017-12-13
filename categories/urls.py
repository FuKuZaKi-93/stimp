from django.conf.urls import url
from . import views


app_name = 'categories'
urlpatterns = [
    url(r'^create/$', views.ThemeCreateView.as_view(), name='create_theme'),
#    url(r'^list/$', views.ThemeListView.as_view(), name='theme_list'),
]
