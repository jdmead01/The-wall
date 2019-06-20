from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.wall),
    url(r'^register$', views.register),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete/(?P<comment_id>\d+)/$', views.delete),
    url(r'^logoff$', views.logoff),
    url(r'^login$', views.login),
]