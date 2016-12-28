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
import requests
import random

# Create your views here.

gpb_amount = {
        'post': 100,
        'get_liked': 10,
        'reply': 20,
        'wanted': 200,
        'normal': 1000,
        'ten': 10000,
        'gold': 20000,
    }

draw_amount = {
    0:1000,
    1:10000,
    2:20000,
}

type_dic = {
    '普通贴':0,
    '提问贴':1,
    '笔记贴':2,
    '回答贴':3,
    '大讨论区':4,
}

sec_dic = {
    'notice':0,
    'complaint':1,
    'chat':2,
    'science':3,
    'engineer':4,
    'pe':5,
    'politics':6,
    'culture':7,
    'english':8,
    'otherlan':9,
    'freeselection':10,
}

title_dic = {
    'notice':"公告区",
    'complaint':"投诉区",
    'chat':"七嘴八舌",
    'science':"理科大讨论",
    'engineer':"工科大讨论",
    'pe':"体育大讨论",
    'politics':"政治大讨论",
    'culture':"文核文素大讨论",
    'english':"英语大讨论",
    'otherlan':"二外大讨论",
    'freeselection':"任选大讨论",
}

level_dic = {
    'R':0,
    'SR':1,
    'UR':2,
}

prop_dic = {
    'UR':1,
    'SR':15
}

mode_dic = {
    '单抽':0,
    '十连':1,
    '黄金抽卡':2
}



def raiseLevel(myuser):
    curlevel = myuser.U_Level
    curgpb = myuser.U_GPB
    thislevelgpb = curlevel*20
    while curgpb >= thislevelgpb:
        myuser.U_Level = myuser.U_Level + 1
        myuser.save()
        thislevelgpb = (myuser.U_Level)*20
    if myuser.U_Level <= 20:
        myuser.U_Honor = "不起眼女主"
    elif myuser.U_Level > 20 and myuser.U_Level <= 40:
        myuser.U_Honor = "咕咕咕"
    elif myuser.U_Level > 40 and myuser.U_Level <= 60:
        myuser.U_Honor = "伊豆的舞女"
    elif myuser.U_Level > 60 and myuser.U_Level <= 80:
        myuser.U_Honor = "清华鸽王"
    elif myuser.U_Level > 80 and myuser.U_Level <= 100:
        myuser.U_Honor = "学堂学家"
    elif myuser.U_Level > 100:
        myuser.U_Honor = "超絶かわいい"
    myuser.save()

def get_courses(user):
    myuser = BBSUser.objects.get(user=user)
    relas = UserHasCourse.objects.filter(UserID=myuser);
    courses = []
    for rela in relas:
        courses.append(rela.CourseID)
    return courses

def bbs_list(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    bestposts = BBSPost.objects.filter(P_Parent=None,P_Type=type_dic['大讨论区'])

    bestposts = list(bestposts)
    bestposts = sorted(bestposts,key=lambda x:x.P_LikeNum,reverse=True)

    posts = bestposts
    courses = get_courses(request.user)
    return render(request, 'index.html',{'posts':posts,'courses':courses})

def update_course_info(studentid):
    response = requests.post('http://se.zhuangty.com:8000/curriculum/'+studentid, data={"apikey": "API Key", "apisecret": "API Secret Key"})
    if response.json()['message'] == 'Success':
        classes = response.json()['classes']
        for eachClass in classes:
            courseid = eachClass['courseid']
            coursename = eachClass['coursename']

            searchCourse = BBSCourse.objects.filter(C_SeqNum=courseid)
            if len(searchCourse) == 0:
                newCourse = BBSCourse()
                newCourse.C_Name = coursename
                newCourse.C_SeqNum = courseid
                newCourse.save()
            UserID = BBSUser.objects.get(U_studentid=studentid)
            CourseID = BBSCourse.objects.get(C_SeqNum=courseid)
            searchCourse = UserHasCourse.objects.filter(UserID=UserID, CourseID=CourseID)
            if len(searchCourse) == 0:
                newUserHasCourse = UserHasCourse()
                newUserHasCourse.UserID = UserID
                newUserHasCourse.CourseID = CourseID
                newUserHasCourse.save()


def validate_user(request,studentid,password):
    response = requests.post('http://se.zhuangty.com:8000/users/register', data={"apikey": "API Key", "apisecret": "API Secret Key", "username": studentid, "password": password})
    if response.json()['message'] == 'Success':
        users = BBSUser.objects.filter(U_studentid=studentid)
        if len(users) == 0:
            newUserSys = User.objects.create_user(username=studentid, password=password)
            newUserSys.save()
            newUserSys = auth.authenticate(username=studentid, password=password)
            auth.login(request, newUserSys)
            newUser = BBSUser()
            newUser.U_studentid = studentid
            newUser.U_password = password
            newUser.user = newUserSys
            newUser.U_RealName = response.json()['information']['realname']
            newUser.U_Major = response.json()['information']['department']
            newUser.save()
            # 这块需要调用接口找到网络学堂的该学生的所有课程然后加到数据库里
            auth.login(request, newUserSys)
            update_course_info(studentid)
            return newUser
        else:
            update_course_info(studentid)
            newUserSys = auth.authenticate(username=studentid, password=password)
            auth.login(request, newUserSys)
            return users[0]
    else:
        return None

def validate_user_bymyself(request,studentid,password):
    test_data = {'i_user': studentid, 'i_pass': password}
    test_data_urlencode = urllib.parse.urlencode(test_data).encode("utf-8")
    requrl = "https://id.tsinghua.edu.cn/do/off/ui/auth/login/post/fa8077873a7a80b1cd6b185d5a796617/0?/j_spring_security_thauth_roaming_entry"
    req = urllib.request.Request(url=requrl, data=test_data_urlencode)
    f = urllib.request.urlopen(req).read().decode('utf8')
    if len(f) >= 2000:
        users = BBSUser.objects.filter(U_studentid=studentid)
        if len(users) == 0:
            newUserSys = User.objects.create_user(username=studentid, password=password)
            newUserSys.save()
            newUserSys = auth.authenticate(username=studentid, password=password)
            auth.login(request, newUserSys)
            newUser = BBSUser()
            newUser.U_studentid = studentid
            newUser.U_password = password
            newUser.user = newUserSys
            newUser.save()
            return newUser
        else:
            newUserSys = auth.authenticate(username=studentid, password=password)
            auth.login(request, newUserSys)
            return users[0]

def login(request):
    # 这里有一个关于学号和id的小bug
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        studentidin = request.POST['studentid']
        passwordin = request.POST['password']
        user = validate_user_bymyself(request,studentid=studentidin, password=passwordin)
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
        hasnotes = 0
        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/login/')

        #print('myuser:',self.request.user)
        myuser = BBSUser.objects.get(user=self.request.user)
        #print('myuser:', myuser)

        posts = BBSPost.objects.filter(P_Course=mycourse,P_Parent=None)

        allnotes = BBSPost.objects.filter(P_Course=mycourse, P_Type=type_dic['笔记贴'])
        if len(allnotes) != 0:
            hasnotes = 1
        mynotesrelas = UserHasNode.objects.filter(UserID=myuser)
        mynotes = []
        posts = list(posts)

        for mynotesrela in mynotesrelas:
            mynotes.append(mynotesrela.PostID)
        newposts = []
        for post in posts:
            if post.P_Type == type_dic['笔记贴'] and (post not in mynotes):
               continue
            if post.P_Type == type_dic['大讨论区']:
                continue
            newposts.append(post)


        context['posts'] = newposts
        context['course'] = mycourse
        context['user'] = myuser
        courses = get_courses(self.request.user)
        context['courses'] = courses
        context['hasnotes'] = hasnotes
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
    if bigpost.P_Type == type_dic['笔记贴'] and len(UserHasNode.objects.filter(UserID=myuser,PostID=bigpost))==0:
        return HttpResponseRedirect('/login/')

    params = request.POST if request.method == 'POST' else None

    form = ReplyForm(params,instance=None)
    if form.is_valid():
        reply_get = form.save(commit=False)
        print(reply_get.P_Title)
        reply = BBSPost()
        reply.P_User = myuser
        reply.P_Title = '回复'
        reply.P_Content = reply_get.P_Content
        reply.P_Course = thiscourse
        reply.P_Type = type_dic['回答贴']
        reply.P_Parent = bigpost
        reply.save()
        myuser.U_GPB += gpb_amount['reply']
        raiseLevel(myuser)
        myuser.save()
        form = ReplyForm(params,instance=None)

    childrenpostsq = BBSPost.objects.filter(P_Parent=bigpost)
    childrenposts=[]
    bestchild = None
    for child in childrenpostsq:
        if child != bigpost.P_BestChild:
            childrenposts.append(child)
        else :
            bestchild = child
    if bestchild != None:
        childrenposts.append(bestchild)
    childrenposts.reverse()

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
    courses = get_courses(request.user)
    context['courses'] = courses
    return render(request,'web/course_bbs_detail.html',context)


def user_self_info(request, param, action):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    visitedUser = User.objects.get(username=param)
    visitedUser = BBSUser.objects.get(user=visitedUser)
    courses = get_courses(request.user)
    #userme = BBSUser.objects.get(user=request.user)
    #courses = get_courses(request.user)
    return render(request,'web/user_self_info.html',{'user':visitedUser, 'courses':courses})

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
        raiseLevel(postuser)
        postuser.save()

    return HttpResponse('follow success')

@csrf_exempt
def post_course_post(request,courseid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    course = BBSCourse.objects.get(id=courseid)
    courses = get_courses(request.user)
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['P_Title'] if request.POST['P_Title'] else ""
        content = request.POST['P_Content'] if request.POST['P_Content'] else ""
        wantedvalue = request.POST['wantedval'] if request.POST['wantedval'] else 0
        realtype = request.POST['Realtype'] if request.POST['Realtype'] else 0
        if not title:
            return render(request,'web/post_post.html',{'error':'请输入帖子题目','P_Title':title,'P_Content':content,'course':course, 'courses':courses})
        if not content:
            return render(request,'web/post_post.html',{'error':'请输入帖子详情','P_Title':title,'P_Content':content,'course':course, 'courses':courses})


        userme = BBSUser.objects.get(user=request.user)

        post = BBSPost()
        post.P_User = userme
        post.P_Title = title
        post.P_Content = content
        post.P_Course = course
        post.P_Type = realtype
        post.P_Wanted = wantedvalue
        post.save()
        userme.U_GPB += gpb_amount['post']
        raiseLevel(userme)
        userme.save()
        return HttpResponseRedirect(reverse('course',args=[courseid]))
    return render(request, 'web/post_post.html', {'course':course, 'courses':courses})

def xuetang_post_detail(request,postid,source):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    myuser = BBSUser.objects.get(user=request.user)
    bigpost = BBSPost.objects.get(id=postid)

    params = request.POST if request.method == 'POST' else None

    form = ReplyForm(params, instance=None)
    if form.is_valid():
        reply_get = form.save(commit=False)
        print(reply_get.P_Title)
        reply = BBSPost()
        reply.P_User = myuser
        reply.P_Title = reply_get.P_Title
        reply.P_Content = reply_get.P_Content
        reply.P_Course = BBSCourse.objects.get(id=1)#此处是错的
        reply.P_Type = type_dic['大讨论区']
        reply.P_Parent = bigpost
        reply.save()
        myuser.U_GPB += gpb_amount['reply']
        raiseLevel(myuser)
        myuser.save()
        form = ReplyForm(params, instance=None)

    childrenposts = BBSPost.objects.filter(P_Parent=bigpost)
    likefilter = UserLikePost.objects.filter(UserID=myuser, PostID=bigpost)
    islike = 0
    if len(likefilter) != 0:
        islike = 1
    context = {}
    context['bigpost'] = bigpost
    context['user'] = myuser
    context['childrenposts'] = childrenposts
    context['islike'] = islike
    context['form'] = form
    context['source'] = source
    courses = get_courses(request.user)
    context['courses'] = courses
    return render(request, 'web/xuetang_bbs_detail.html', context)

def post_xuetang_post_detail(request,source):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    courses = get_courses(request.user)
    if request.method == 'POST':
        title = request.POST['P_Title'] if request.POST['P_Title'] else ""
        content = request.POST['P_Content'] if request.POST['P_Content'] else ""
        if not title:
            return render(request,'web/post_xuetang_post.html',{'error':'请输入帖子题目','P_Title':title,'P_Content':content, 'courses':courses})
        if not content:
            return render(request,'web/post_xuetang_post.html',{'error':'请输入帖子详情','P_Title':title,'P_Content':content, 'courses':courses})
        if not type:
            return render(request,'web/post_xuetang_post.html',{'error':'请选择帖子类别','P_Title': title,'P_Content': content, 'courses':courses})

        userme = BBSUser.objects.get(user=request.user)

        post = BBSPost()
        post.P_User = userme
        post.P_Title = title
        post.P_Content = content
        post.P_Course = BBSCourse.objects.get(id=1)#此处是错的
        post.P_Type = type_dic['大讨论区']
        post.P_Section = sec_dic[source]
        post.save()
        userme.U_GPB += gpb_amount['post']
        raiseLevel(userme)
        userme.save()
        return HttpResponseRedirect("/"+source+"/")

    return render(request, 'web/post_xuetang_post.html',{'source':source,'courses':courses})

def xuetang_notice(request,source):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    myuser = BBSUser.objects.get(user=request.user)
    print("KeyError",type_dic['大讨论区'],sec_dic[source])
    bestposts = BBSPost.objects.filter(P_Parent=None, P_Type=type_dic['大讨论区'],P_Section=sec_dic[source])
    bestposts = list(bestposts)
    bestposts = sorted(bestposts, key=lambda x: x.P_Time, reverse=True)
    posts = bestposts
    courses = get_courses(request.user)
    return render(request, 'web/xuetang_list.html', {'user':myuser,'posts': posts,'title':title_dic[source],'source':source,'courses':courses})

def delete_post(request,courseid,postid,parentid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    postde = BBSPost.objects.get(id=postid)
    likes = UserLikePost.objects.filter(PostID=postde)
    follows = UserFollowPost.objects.filter(PostID=postde)
    for like in likes:
        like.delete()
    for follow in follows:
        follow.delete()
    postde.delete()
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['reply']
    myuser.save()
    return HttpResponseRedirect("/course/"+str(courseid)+"/post/"+str(parentid)+"/")

def delete_bigpost(request,courseid,postid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    postde = BBSPost.objects.get(id=postid)
    likes = UserLikePost.objects.filter(PostID=postde)
    follows = UserFollowPost.objects.filter(PostID=postde)
    for like in likes:
        like.delete()
    for follow in follows:
        follow.delete()
    postde.delete()
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['post']
    myuser.save()
    return HttpResponseRedirect("/course/" + str(courseid) + "/")

def delete_xuetang_post(request,parentid,source,postid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    postde = BBSPost.objects.get(id=postid)
    likes = UserLikePost.objects.filter(PostID=postde)
    follows = UserFollowPost.objects.filter(PostID=postde)
    for like in likes:
        like.delete()
    for follow in follows:
        follow.delete()
    postde.delete()
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['reply']
    myuser.save()
    return HttpResponseRedirect("/xpostdetail/"+str(parentid)+"/"+source+"/")

def delete_xuetang_bigpost(request,source,postid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    postde = BBSPost.objects.get(id=postid)
    likes = UserLikePost.objects.filter(PostID=postde)
    follows = UserFollowPost.objects.filter(PostID=postde)
    for like in likes:
        like.delete()
    for follow in follows:
        follow.delete()
    postde.delete()
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['post']
    myuser.save()
    return HttpResponseRedirect("/"+source+"/")

def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.user.is_authenticated():
        auth.logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')

@csrf_exempt
def good_post(request,courseid,bigpostid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        goodpostid = int(request.POST['postID'])
        parentid = int(request.POST['parentID'])
        goodpost = BBSPost.objects.get(id=goodpostid)
        parent = BBSPost.objects.get(id=parentid)
        if parent.P_BestChild != None:
            if parent.P_BestChild == goodpost:
                parent.P_BestChild.P_User.U_GPB -= parent.P_Wanted
                parent.P_BestChild.P_User.save()
                parent.P_BestChild = None
                parent.save()
                return HttpResponseRedirect("/course/"+courseid+"/post/"+bigpostid+"/")
            else:
                parent.P_BestChild.P_User.U_GPB -= parent.P_Wanted
                parent.P_BestChild.P_User.save()
        parent.P_BestChild = goodpost
        #print("good:",goodpost.P_Content)
        parent.save()
        goodpost.P_User.U_GPB += parent.P_Wanted
        raiseLevel(goodpost.P_User)
        goodpost.P_User.save()
        parent.P_User.U_GPB -= parent.P_Wanted
        parent.P_User.save()
        return HttpResponseRedirect("/course/" + courseid + "/post/" + bigpostid + "/")
    return HttpResponseRedirect("/course/"+courseid+"/post/"+bigpostid+"/")


@csrf_exempt
def ajax_append_image(request):
    data = request.FILES['file']
    path = default_storage.save(data.name, ContentFile(data.read()))
    return HttpResponse(path)

@csrf_exempt
def ajax_change_image(request):
    file = request.FILES if request.method == 'POST' else None
    bbsuser = BBSUser.objects.get(user=request.user)
    if file:
        bbsuser.U_Image = file['file']
        bbsuser.save()
    return HttpResponse(bbsuser.U_Image)

def draw_note(request,courseid,modeid):
    courses = get_courses(request.user)
    course = BBSCourse.objects.get(id=courseid)
    myuser = BBSUser.objects.get(user=request.user)
    allnotes = BBSPost.objects.filter(P_Course=course,P_Type=type_dic['笔记贴'])

    if allnotes == []:
        return render(request,"web/course_drawing.html",{'user':myuser,'courses':courses,'course':course,'iserror':1,'modeid':modeid,'error':"没有笔记贴可抽！"})
    if myuser.U_GPB < draw_amount[int(modeid)]:
        return render(request, "web/course_drawing.html",
                      {'user': myuser, 'courses': courses, 'course': course, 'iserror': 1, 'modeid': modeid,
                       'error': "GPB不够哦！"})
    return render(request, "web/course_drawing.html", {'user': myuser, 'courses': courses, 'course': course, 'iserror': 0,'modeid':modeid})

def draw_one(course):
    noterand = random.randint(1, 100)
    allnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'])
    getnote = None
    if noterand >= 1 and noterand <= prop_dic['UR']:
        urnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'], P_Level=level_dic['UR'])
        if len(urnotes) == 0:
            noterand = random.randint(prop_dic['UR'] + 1, 100)
        else:
            siterand = random.randint(0, len(urnotes) - 1)
            print("UR", len(urnotes), siterand)
            getnote = urnotes[siterand]
    if noterand >= prop_dic['UR'] + 1 and noterand <= prop_dic['UR'] + prop_dic['SR']:
        srnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'], P_Level=level_dic['SR'])
        if len(srnotes) == 0:
            noterand = random.randint(prop_dic['UR'] + prop_dic['SR'] + 1, 100)
        else:
            siterand = random.randint(0, len(srnotes) - 1)
            print("SR", len(srnotes), siterand)
            getnote = srnotes[siterand]
    if noterand >= prop_dic['UR'] + prop_dic['SR'] + 1:
        rnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'], P_Level=level_dic['R'])
        if len(rnotes) == 0:
            getnote = allnotes[0]
        else:
            siterand = random.randint(0, len(rnotes) - 1)
            print("R", len(rnotes), siterand)
            getnote = rnotes[siterand]
    return getnote

def draw_good(course):
    noterand = random.randint(1, prop_dic['UR'] + prop_dic['SR'])
    allnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'])
    urnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'], P_Level=level_dic['UR'])
    srnotes = BBSPost.objects.filter(P_Course=course, P_Type=type_dic['笔记贴'], P_Level=level_dic['SR'])
    if len(urnotes) == 0 or len(srnotes) == 0:
        return None
    getnote = None
    if noterand >= 1 and noterand <= prop_dic['UR']:
        if len(urnotes) == 0:
            noterand = random.randint(prop_dic['UR'] + 1, prop_dic['UR'] + prop_dic['SR'])
        else:
            siterand = random.randint(0, len(urnotes) - 1)
            getnote = urnotes[siterand]
    if noterand >= prop_dic['UR'] + 1 and noterand <= prop_dic['UR'] + prop_dic['SR']:
        if len(srnotes) == 0:
            getnote = urnotes[0]
        else:
            siterand = random.randint(0, len(srnotes) - 1)
            getnote = srnotes[siterand]
    return getnote

def draw_10(course):
    getnotes=[]
    insertrand = random.randint(0,9)
    for i in range(0,10):
        if i == insertrand:
            getnotegood = draw_good(course)
            if getnotegood == None:
                i -=1
                continue
            getnotes.append(getnotegood)
            continue
        getnote = draw_one(course)
        getnotes.append(getnote)
    return getnotes


def get_result(request,courseid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    courses = get_courses(request.user)
    course = BBSCourse.objects.get(id=courseid)
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['normal']
    myuser.save()
    getnote = draw_one(course)
    if len(UserHasNode.objects.filter(UserID=myuser,PostID=getnote)) == 0:
        userhasnote = UserHasNode(UserID=myuser,PostID=getnote)
        userhasnote.save()
    posts = [getnote]
    context={}
    context['posts'] = posts
    context['course'] = course
    context['user'] = myuser
    context['courses'] = courses
    context['hasnotes'] = 1
    return render(request, 'web/course_bbs_list.html', context)

def get_result10(request,courseid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    courses = get_courses(request.user)
    course = BBSCourse.objects.get(id=courseid)
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['ten']
    myuser.save()
    getnotes = draw_10(course)
    for getnote in getnotes:
        if len(UserHasNode.objects.filter(UserID=myuser, PostID=getnote)) == 0:
            userhasnote = UserHasNode(UserID=myuser, PostID=getnote)
            userhasnote.save()
    posts = getnotes
    context={}
    context['posts'] = posts
    context['course'] = course
    context['user'] = myuser
    context['courses'] = courses
    context['hasnotes'] = 1
    return render(request, 'web/course_bbs_list.html', context)

def get_resultgood(request,courseid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    courses = get_courses(request.user)
    course = BBSCourse.objects.get(id=courseid)
    myuser = BBSUser.objects.get(user=request.user)
    myuser.U_GPB -= gpb_amount['gold']
    myuser.save()
    getnote = draw_good(course)
    if len(UserHasNode.objects.filter(UserID=myuser,PostID=getnote)) == 0:
        userhasnote = UserHasNode(UserID=myuser,PostID=getnote)
        userhasnote.save()
    posts = [getnote]
    context={}
    context['posts'] = posts
    context['course'] = course
    context['user'] = myuser
    context['courses'] = courses
    context['hasnotes'] = 1
    return render(request, 'web/course_bbs_list.html', context)

def user_self_like(request,userid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    myuser = BBSUser.objects.get(user=request.user)
    courses = get_courses(request.user)
    thisuser = BBSUser.objects.get(id=userid)
    thisrelas = UserLikePost.objects.filter(UserID=thisuser)
    thisposts = []
    for thisrela in thisrelas:
        if thisrela.PostID.P_Course not in courses:
            continue
        thisposts.append(thisrela.PostID)
    return render(request,'web/search_list.html',{'courses':courses,'posts':thisposts,'info':"点赞"})

def user_self_ask(request,userid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    myuser = BBSUser.objects.get(user=request.user)
    courses = get_courses(request.user)
    thisuser = BBSUser.objects.get(id=userid)
    hisposts = BBSPost.objects.filter(P_User = thisuser,P_Type = type_dic['提问贴'])
    thisposts = []
    for hispost in hisposts:
        if hispost.P_Course not in courses:
            continue
        thisposts.append(hispost)
    return render(request,'web/search_list.html',{'courses':courses,'posts':thisposts,'info':"提问"})

def user_self_answer(request,userid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    myuser = BBSUser.objects.get(user=request.user)
    courses = get_courses(request.user)
    thisuser = BBSUser.objects.get(id=userid)
    hisposts = BBSPost.objects.filter(P_User = thisuser,P_Type = type_dic['回答贴'])
    thisposts = []
    for hispost in hisposts:
        if hispost.P_Course not in courses:
            continue
        thisposts.append(hispost.P_Parent)
    return render(request,'web/search_list.html',{'courses':courses,'posts':thisposts,'info':"回答"})

#test




