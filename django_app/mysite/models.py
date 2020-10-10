from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime 

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    SELECTION = ((0,'無し'),(1,'仮登録'),(2,'本登録'))
    user = models.ForeignKey(User,verbose_name='ユーザ',related_name='user4',on_delete=models.CASCADE)
    mailaddress = models.EmailField('メールアドレス',max_length=255, default="address here")
    address_status = models.IntegerField('登録有無',choices=SELECTION, default=0)
    status = models.IntegerField('メール送信状態',default=0)
    def __str__(self):
        return self.user.username

class CoursesTaken(models.Model):
    SELECTION = ((2,'月曜日'),(3,'火曜日'),(4,'水曜日'),(5,'木曜日'),(6,'金曜日',),(7,'土曜日'))
    SELECTION1 = ((1,'１限'),(2,'2限'),(3,'3限'),(4,'4限'),(5,'5限'),(6,'6限'),(7,'7限'))
    name = models.CharField('履修科目名',max_length=255)
    CT_status = models.IntegerField('曜日',choices=SELECTION)
    period = models.IntegerField('時限',choices=SELECTION1)
    URLURL = models.CharField('授業用URL',max_length=100,default ="#")
    school_credit = models.IntegerField('単位数',default=0)
    
    class meta:
        unique_together = (('CT_status','period'))

    def __str__(self):
        return self.name

class UserCTInfo(models.Model):
    SELECTION = ((0,'未履修'),(1,'履修中'))
    user = models.ForeignKey(User,verbose_name='ユーザ',related_name='user',on_delete=models.CASCADE)
    CT = models.ForeignKey(CoursesTaken,verbose_name='科目',related_name='use_CT_info',on_delete=models.CASCADE)
    user_CT = models.IntegerField('履修状態',choices=SELECTION)
    
    def __str__(self):
        return self.user.username

dt_now = datetime.datetime.now()

class KadaiInfo(models.Model):
    SELECTION = ((0,'使用'), (1,'使用しない'))
    CT = models.ForeignKey(CoursesTaken,verbose_name='科目',related_name='kadai_info',on_delete=models.CASCADE)
    name = models.CharField('課題名',max_length=255)
    date = models.DateTimeField('提出期日', default="2020-10-08 12:00")
    overview = models.CharField('概要', max_length = 1000)
    display = models.IntegerField('表示・非表示', choices=SELECTION ,default=0) #削除の時に使用
    submit_date = models.DateTimeField('提出した日',null=True)
    def __str__(self):
        return self.name

class UserKadaiInfo(models.Model):
    SELECTION = ((0,'未提出'),(1,'提出済'))
    KI = models.ForeignKey(KadaiInfo,verbose_name='課題',related_name='user_kadai_info',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='ユーザ',related_name='user1',on_delete=models.CASCADE)
    point = models.IntegerField('この課題で取得した点数', default=0)
    status = models.IntegerField('提出状況', choices = SELECTION)
    def __str__(self):
        return self.user.username

class TestInfo(models.Model):
    CT = models.ForeignKey(CoursesTaken,verbose_name='科目',related_name='test_info',on_delete=models.CASCADE)
    name = models.CharField('テスト名',max_length=255)
    date = models.DateTimeField('テスト日',)
    overview = models.CharField('概要', max_length = 1000)
    def __str__(self):
        return self.name

class UserTestInfo(models.Model):
    SELECTION = ((0,'未受験'),(1,'受験済み'))
    TI = models.ForeignKey(TestInfo,verbose_name='テスト',related_name='user_test_info',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='ユーザ',related_name='user2',on_delete=models.CASCADE)
    point = models.IntegerField('このテストで取得した点数', default=0)
    status = models.IntegerField('提出状況', choices = SELECTION)
    def __str__(self):
        return self.user.username