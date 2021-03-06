from django.conf.urls import url
from . import views
from .views import *
urlpatterns = [
    url(r'^$', views.bbs_list, name='index'),
    url(r'^course/(\d+)/$', views.course_post_list,name='course'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^course/(\d+)/post/(\d+)/$',views.course_post_detail),
    url(r'^me/(\w+)/(\w*)$',views.user_self_info,name='me'),
    url(r'^helikes/(\d+)/$',views.user_self_like),
    url(r'^heasks/(\d+)/$',views.user_self_ask),
    url(r'^heanswers/(\d+)/$',views.user_self_answer),
    url(r'^like_post_deal/$', views.like_post_deal),
    url(r'^course/(\d+)/delete_post/(\d+)/parentpost/(\d+)/$', views.delete_post),
    url(r'^course/(\d+)/delete_post/(\d+)/$', views.delete_bigpost),
    url(r'^course/(\d+)/drawing/(\d+)/$',views.draw_note),
    url(r'^course/(\d+)/result/$',views.get_result),
    url(r'^course/(\d+)/result10/$',views.get_result10),
    url(r'^course/(\d+)/resultgood/$',views.get_resultgood),
    url(r'^post/(\d+)/$',views.post_course_post,name='newpost'),
    url(r'^good/(\d+)/(\d+)/$',views.good_post),
    url(r'^xpostdetail/(\d+)/(\w+)/$',views.xuetang_post_detail),
    url(r'^xpostdetail/(\d+)/(\w+)/delete_post/(\d+)/$',views.delete_xuetang_post),
    url(r'^(\w+)/delete_post/(\d+)/$',views.delete_xuetang_bigpost),
    url(r'^postxpostdetail/(\w+)/$',views.post_xuetang_post_detail),
    url(r'^ajax_change_nickname/$', views.ajax_change_nickname),
    url(r'^ajax_append_image/$', views.ajax_append_image),
    url(r'^ajax_change_image/$', views.ajax_change_image),
    url(r'^(\w+)/$',views.xuetang_notice),
]
