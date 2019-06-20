from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.wall),
    url(r'^register$', views.register),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete/comment/(?P<comment_id>\d+)/$', views.delete_comment),
    url(r'^delete/message/(?P<message_id>\d+)/$', views.delete_message),
    url(r'^logoff$', views.logoff),
    url(r'^login$', views.login),
]