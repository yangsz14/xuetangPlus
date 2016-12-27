from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BBSUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    U_studentid = models.CharField(max_length=15)
    U_password = models.CharField(max_length=100)
    U_name = models.CharField(blank=True,max_length=50)
    U_RealName = models.CharField(blank=True,max_length=50)
    U_Honor = models.CharField(blank=True, max_length=50)
    U_Major = models.TextField(blank=True)
    U_Description = models.TextField(null=True, blank=True)
    U_Image = models.ImageField(null=True, blank=True)
    U_Identity = models.IntegerField(default=1)
    U_Level = models.IntegerField(default=0)
    U_GPB = models.IntegerField(default=0)
    U_FollowUserNum = models.IntegerField(default=0)
    U_FollowPostNum = models.IntegerField(default=0)
    U_PostNum = models.IntegerField(default=0)
    U_QuestionNum = models.IntegerField(default=0)
    U_AnswerNum = models.IntegerField(default=0)

    def __str__(self):
        return self.U_studentid


class BBSCourse(models.Model):
    C_Name = models.CharField(max_length=100)
    C_SeqNum = models.CharField(blank=True,max_length=50)

    def __str__(self):
        return self.C_Name

class BBSPost(models.Model):
    P_User = models.ForeignKey(BBSUser)  # 帖子作者关系
    P_Course = models.ForeignKey(BBSCourse)
    P_Type = models.IntegerField(default=0)
    P_Title = models.CharField(max_length=100, blank=True)
    P_Content = models.TextField()
    P_Time = models.DateTimeField(default=timezone.now)
    P_LastComTime = models.DateTimeField(default=timezone.now)
    P_LikeNum = models.IntegerField(default=0)
    P_Section = models.IntegerField(default=1)
    P_Parent = models.ForeignKey('self', blank=True, null=True,related_name="child")
    P_ReplyNum = models.IntegerField(default=0)
    P_Top = models.IntegerField(default=0)
    P_Wanted = models.IntegerField(default=0)
    P_BestChild = models.ForeignKey('self',blank=True,default=None,null=True,related_name="parent")
    P_Level = models.IntegerField(default=0)

    def __str__(self):
        return self.P_Title



class FollowUser(models.Model):
    User1ID = models.ForeignKey(BBSUser, related_name='follower')
    User2ID = models.ForeignKey(User, related_name='followee')

class UserLikePost(models.Model):
    UserID = models.ForeignKey(BBSUser)
    PostID = models.ForeignKey(BBSPost)

class UserFollowPost(models.Model):
    UserID = models.ForeignKey(BBSUser)
    PostID = models.ForeignKey(BBSPost)

class UserHasCourse(models.Model):
    UserID = models.ForeignKey(BBSUser)
    CourseID = models.ForeignKey(BBSCourse)

class UserHasNode(models.Model):
    UserID = models.ForeignKey(BBSUser)
    PostID = models.ForeignKey(BBSPost)