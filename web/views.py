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

# Create your views here.

def bbs_list(request):
    return render(request, 'index.html')


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
        posts = BBSPost.objects.filter(P_User=myuser, P_Course=mycourse)
        context['posts'] = posts
        context['course'] = mycourse
        context['user'] = myuser
        return context

class CoursePostDetailView(ListView):

    model = BBSPost
    template_name = 'web/course_bbs_detail.html'
    pk_courseid_kwarg = 'courseid'
    pk_postid_kwarg = 'postid'

    def get_context_data(self,**kwargs):
        posts = BBSPost.objects.all()
        print(posts[0].id)
        context = super(CoursePostDetailView, self).get_context_data(**kwargs)
        courseid = int(self.kwargs.get(self.pk_courseid_kwarg, None))
        thiscourse = BBSCourse.objects.get(id=courseid)
        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        myuser = BBSUser.objects.get(user=self.request.user)
        postid = int(self.kwargs.get(self.pk_postid_kwarg, None))
        bigpost = BBSPost.objects.get(id=postid,P_Course=thiscourse)
        childrenposts = BBSPost.objects.filter(P_Parent=bigpost)
        context['bigpost'] = bigpost
        context['course'] = thiscourse
        context['user'] = myuser
        context['childrenposts'] = childrenposts
        return context


