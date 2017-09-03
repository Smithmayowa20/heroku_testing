from django.conf.urls import url
from . import views
from django.views.generic import (TemplateView, 
    RedirectView,
)
from django.conf import settings
urlpatterns = [url(r'^profile/edit/$',views.edit_profile_page,name='edit_profile_page'),
url(r'^new/post/(?P<category>[-\w]+)/$',views.new_post, name='new_post'),
url(r'^follow/(?P<user1>[-\w]+)$',views.follow,name='follow'),
url(r'^detail/post/(?P<pk>\d+)$',views.post_detail,name='post_detail'),
url(r'^post/new-comment/(?P<slug>[-\w]+)/$', views.new_comment1, name='new_comment1'),
url(r'^post/new-comment/(?P<pk>\d+)/(?P<position>\d+)/(?P<parent_no>\d+)/$', views.new_comment, name='new_comment'),
url(r'^profile/$',views.profile_page,name='profile_page'),
url(r'^profile/(?P<user>[-\w]+)$',views.profile_page,name='profile_page2'),
url(r'^$',views.landing_page,name='landing_page'),
url(r'^home/$',views.user_feed,name='user_feed'),
url(r'^category/(?P<category>[-\w]+)$',views.genre_category,name='genre_category'),]