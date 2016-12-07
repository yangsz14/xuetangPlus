from django.conf.urls import url
from . import views
from .views import *
urlpatterns = [
    url(r'^$', views.bbs_list, name='index'),
    url(r'^course/(?P<courseid>\d+)/$', CoursePostListView.as_view(),name='course'),
    url(r'^login/$',views.login,name='login'),
    url(r'^course/(?P<courseid>\d+)/post/(?P<postid>\d+)/$',CoursePostDetailView.as_view()),
    url(r'^me/$',views.user_self_info,name='me'),
    url(r'^like_post_deal/$', views.like_post_deal),
    url(r'^post/(\d+)/$',views.post_course_post,name='newpost'),
    #迭代一前请写一下用户修改个人信息的页面，麻烦了
    #迭代一前请写一下用户发帖的页面，麻烦了
]
