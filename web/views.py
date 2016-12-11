from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
from django.utils import timezone
import json
from django.http import HttpResponse
from django.views.generic import View
from codex.baseerror import *
import urllib.request
from django.contrib import auth
from .models import *
from django.views.generic.detail import *
from django.views.generic.list import *
from django.core.urlresolvers import reverse
from .forms import *

# Create your views here.

gpb_amount = {
        'post': 100,
        'get_liked': 10,
        'reply': 20,
    }

type_dic = {
    '普通贴':0,
    '提问贴':1,
    '笔记贴':2,
    '回答贴':3,
    '大讨论区':4,
}

def bbs_list(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    bestposts = BBSPost.objects.filter(P_Parent=None,P_Type=type_dic['大讨论区'])
    bestposts = list(bestposts)
    bestposts = sorted(bestposts,key=lambda x:x.P_LikeNum,reverse=True)
    posts = bestposts[1:10]
    return render(request, 'index.html',{'posts':posts})


def validate_user(request,studentid,password):
    test_data = {'i_user': studentid, 'i_pass': password}
    test_data_urlencode = urllib.parse.urlencode(test_data).encode("utf-8")
    requrl = "https://id.tsinghua.edu.cn/do/off/ui/auth/login/post/fa8077873a7a80b1cd6b185d5a796617/0?/j_spring_security_thauth_roaming_entry"
    req = urllib.request.Request(url=requrl, data=test_data_urlencode)

    f = urllib.request.urlopen(req).read().decode('utf8')
    if len(f) >= 2000:
        users = BBSUser.objects.filter(U_studentid = studentid)
        if len(users) == 0:
            newUserSys = User.objects.create_user(username=studentid, password=password)
            newUserSys.save()
            newUserSys = auth.authenticate(username=studentid, password=password)
            newUser = BBSUser()
            newUser.U_studentid = studentid
            newUser.U_password = password
            newUser.user = newUserSys
            newUser.save()

            # 这块需要调用接口找到网络学堂的该学生的所有课程然后加到数据库里
            # 这块需要搞来学生的名字，专业等真实信息
            return newUser
        else:
            newUserSys = auth.authenticate(username=studentid, password=password)
            auth.login(request, newUserSys)
            return users[0]
    else:
        return None


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        studentidin = request.POST['studentid']
        passwordin = request.POST['password']
        user = validate_user(request,studentid=studentidin, password=passwordin)
        if user is not None:
            return HttpResponseRedirect('/')
        else:
            return render(request, "web/login.html", {'error': "学号或密码不正确"})
    else:
        return render(request, "web/login.html")

class CoursePostListView(ListView):

    model = BBSPost
    template_name = 'web/course_bbs_list.html'
    pk_courseid_kwarg = 'courseid'

    def get_context_data(self,**kwargs):

        context = super(CoursePostListView,self).get_context_data(**kwargs)
        courseid = int(self.kwargs.get(self.pk_courseid_kwarg, None))
        #print('mycourseid:', courseid)
        mycourse = BBSCourse.objects.get(id=courseid)
        #print('mycourse:', mycourse)
        #print('myuser:', self.request.user)

        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/login/')

        #print('myuser:',self.request.user)
        myuser = BBSUser.objects.get(user=self.request.user)
        #print('myuser:', myuser)

        posts = BBSPost.objects.filter(P_User=myuser, P_Course=mycourse,P_Parent=None)
        context['posts'] = posts
        context['course'] = mycourse
        context['user'] = myuser
        print("3")

        return context

# class CoursePostDetailView(ListView):
#
#     model = BBSPost
#     template_name = 'web/course_bbs_detail.html'
#     pk_courseid_kwarg = 'courseid'
#     pk_postid_kwarg = 'postid'
#
#     def get_context_data(self,**kwargs):
#         context = super(CoursePostDetailView, self).get_context_data(**kwargs)
#         courseid = int(self.kwargs.get(self.pk_courseid_kwarg, None))
#         thiscourse = BBSCourse.objects.get(id=courseid)
#         if not self.request.user.is_authenticated():
#             return HttpResponseRedirect('/login/')
#         myuser = BBSUser.objects.get(user=self.request.user)
#         postid = int(self.kwargs.get(self.pk_postid_kwarg, None))
#         bigpost = BBSPost.objects.get(id=postid,P_Course=thiscourse)
#
#         params = self.request.POST if self.request.method == 'POST' else None
#
#         form = ReplyForm(params)
#         if form.is_valid():
#             reply_get = form.save(commit=False)
#             print(reply_get.P_Title)
#             reply = BBSPost()
#             reply.P_User = myuser
#             reply.P_Title = reply_get.P_Title
#             reply.P_Content = reply_get.P_Content
#             reply.P_Type = 3
#             reply.P_Parent = bigpost
#             reply.save()
#             form = ReplyForm(params)
#
#         childrenposts = BBSPost.objects.filter(P_Parent=bigpost)
#         likefilter = UserLikePost.objects.filter(UserID=myuser,PostID=bigpost)
#         islike = 0
#         if len(likefilter) != 0:
#             islike = 1
#
#         context['bigpost'] = bigpost
#         context['course'] = thiscourse
#         context['user'] = myuser
#         context['childrenposts'] = childrenposts
#         context['islike'] = islike
#         context['form'] = form
#         return context

# class UserDetailView(DetailView):
#
#     model = BBSUser
#     template_name = 'web/user_self_info.html'
#
#     def get_context_data(self,**kwargs):
#         context = super(UserDetailView, self).get_context_data(**kwargs)
#         if not self.request.user.is_authenticated():
#             return HttpResponseRedirect('/login/')
#         userme = BBSUser.objects.get(user=self.request.user)
#         context['user'] = userme
#         return context

def course_post_detail(request,courseid,postid):
    thiscourse = BBSCourse.objects.get(id=courseid)
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    myuser = BBSUser.objects.get(user=request.user)
    bigpost = BBSPost.objects.get(id=postid, P_Course=thiscourse)

    params = request.POST if request.method == 'POST' else None

    form = ReplyForm(params,instance=None)
    if form.is_valid():
        reply_get = form.save(commit=False)
        print(reply_get.P_Title)
        reply = BBSPost()
        reply.P_User = myuser
        reply.P_Title = reply_get.P_Title
        reply.P_Content = reply_get.P_Content
        reply.P_Course = thiscourse
        reply.P_Type = 3
        reply.P_Parent = bigpost
        reply.save()
        myuser.U_GPB += gpb_amount['reply']
        myuser.save()
        form = ReplyForm(params,instance=None)

    childrenposts = BBSPost.objects.filter(P_Parent=bigpost)
    likefilter = UserLikePost.objects.filter(UserID=myuser, PostID=bigpost)
    islike = 0
    if len(likefilter) != 0:
        islike = 1
    context = {}
    context['bigpost'] = bigpost
    context['course'] = thiscourse
    context['user'] = myuser
    context['childrenposts'] = childrenposts
    context['islike'] = islike
    context['form'] = form
    return render(request,'web/course_bbs_detail.html',context)


def user_self_info(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    userme = BBSUser.objects.get(user=request.user)
    return render(request,'web/user_self_info.html',{'user':userme})

@csrf_exempt
def like_post_deal(request):
    userme = BBSUser.objects.get(user=request.user)
    post = BBSPost.objects.get(id=int(request.POST['postID']))
    postuser = BBSUser.objects.get(id=post.P_User.id)
    if UserLikePost.objects.filter(UserID=userme.id, PostID=post).exists():
        UserLikePost.objects.get(UserID=userme.id, PostID=post).delete()
        post.P_LikeNum -= 1
        post.save()
        postuser.U_GPB -= gpb_amount['get_liked']
        postuser.save()
    else:
        newLikePost = UserLikePost()
        newLikePost.UserID = userme
        newLikePost.PostID = post
        newLikePost.save()
        post.P_LikeNum += 1
        post.save()
        postuser.U_GPB += gpb_amount['get_liked']
        postuser.save()

    return HttpResponse('follow success')

def post_course_post(request,courseid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    course = BBSCourse.objects.get(id=courseid)
    if request.method == 'POST':
        title = request.POST['P_Title'] if request.POST['P_Title'] else ""
        content = request.POST['P_Content'] if request.POST['P_Content'] else ""
        type = request.POST['P_Type'] if request.POST['P_Type'] else 0

        if not title:
            return render(request,'web/post_post.html',{'error':'请输入帖子题目','P_Title':title,'P_Content':content,'P_Type':type,'course':course})
        if not content:
            return render(request,'web/post_post.html',{'error':'请输入帖子详情','P_Title':title,'P_Content':content,'P_Type':type,'course':course})
        if not type:
            return render(request,'web/post_post.html',{'error':'请选择帖子类别','P_Title': title,'P_Content': content,'P_Type': type,'course':course})

        userme = BBSUser.objects.get(user=request.user)

        post = BBSPost()
        post.P_User = userme
        post.P_Title = title
        post.P_Content = content
        post.P_Course = course
        post.P_Type = type
        post.save()
        userme.U_GPB += gpb_amount['post']#暂时立即数
        userme.save()
        return HttpResponseRedirect(reverse('course',args=[courseid]))
    return render(request, 'web/post_post.html', {'course':course})



