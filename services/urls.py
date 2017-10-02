from django.conf.urls import url
from . import views
from django.views.generic import (TemplateView, 
    RedirectView,
)
from django.conf import settings
urlpatterns = [url(r'^profile/create/$',views.create_profile_page,name='create_profile_page'),
url(r'^profile/edit/(?P<slug>[-\w]+)/$',views.profile_page_edit,name='profile_page_edit'),
url(r'^new/post/(?P<category>[-\w]+)/$',views.new_post, name='new_post'),
url(r'^follow/(?P<user1>[-\w]+)$',views.follow,name='follow'),
url(r'^unfollow/(?P<user1>[-\w]+)$',views.unfollow,name='unfollow'),
url(r'^genre/follow/(?P<category>[-\w]+)/$',views.genre_follow,name='genre_follow'),
url(r'^genre/unfollow/(?P<category>[-\w]+)/$',views.genre_unfollow,name='genre_unfollow'),
url(r'^detail/post/(?P<pk>\d+)$',views.post_detail,name='post_detail'),
url(r'^post/new-comment/(?P<slug>[-\w]+)/$', views.new_comment1, name='new_comment1'),
url(r'^post/new-comment/(?P<pk>\d+)/(?P<position>\d+)/(?P<parent_no>\d+)/$', views.new_comment, name='new_comment'),
url(r'^profile/$',views.profile_page,name='profile_page'),
url(r'^profile/(?P<user>[-\w]+)$',views.profile_page,name='profile_page2'),
url(r'^home/$',views.user_feed,name='user_feed'),
url(r'^category/$',views.all_categories,name="all_categories"),
url(r'^category/(?P<category>[-\w]+)/$',views.genre_category,name="genre_category"),
url(r'^.*$',views.landing_page,name='landing_page'),]