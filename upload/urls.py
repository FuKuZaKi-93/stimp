from django.conf.urls import url
from .views import index, main_list
from django.contrib.auth.decorators import login_required
#from .views import ImgDeleteView

app_name = 'upload'
urlpatterns = [
#    url(r'^$', views.form, name='index'),
    url(r'^top/$', main_list.ImgIndexView.as_view(), name='main_list'),
    url(r'^mypage/$', login_required(index.ImgMyListView.as_view()), name='mypage'),
    url(r'^upload/create/$', index.ImgCreateUserView.as_view(), name='create'),
    url(r'^upload/update/(?P<pk>[0-9]+)/$',
        index.ImgUpdateView.as_view(), name='update'),
    url(r'^upload/delete/(?P<pk>[0-9]+)/$',
        index.ImgDeleteView.as_view(), name='delete'),
#    url(r'^event01/$', index.ImgEvent01View.as_view(), name='event01'),
#    url(r'^detail/(?P<pk>[0-9]+)/$', index.ImgDetailWithCommentView.as_view(), name='detail'),

#    url(r'^situation/$', index.SituationCreate.as_view(), name='situation'),
]


