from django import forms
from .models import CoursesTaken,UserCTInfo, KadaiInfo, UserKadaiInfo, TestInfo, UserTestInfo,UserInfo
class UserForm(forms.ModelForm):
    class Meta:
        model = CoursesTaken
        fields = ('name', 'CT_status','period','URLURL','school_credit')
        labels = {
            'name': '名前',
            'CT_status': '曜日',
            'period':'時限',
            'URLURL':'授業用URL',
            'school_credit':'単位数'
        }

class UserForm1(forms.ModelForm):
    class Meta:
        model = UserCTInfo
        fields = ('user_CT',)
        labels = {
            'user_CT': '履修状態'
        }

class KIForm(forms.ModelForm):
    class Meta:
        model = KadaiInfo
        fields = ('CT','name', 'date', 'overview')
        labels = {
            'CT': '科目名',
            'name': '課題名',
            'date': '提出期日(例：2020-1-1 12:00)',
            'overview': '概要'
        }

class UKIForm(forms.ModelForm):
    class Meta:
        model = UserKadaiInfo
        fields = ('point','status')
        labels = {
            'point': 'この課題で取得した点数',
            'status': '提出状況'
        }

class TIForm(forms.ModelForm):
    class Meta:
        model = TestInfo
        fields = ('CT','name', 'date', 'overview')
        labels = {
            'CT': '科目名',
            'name': 'テスト名',
            'date': 'テスト日(例：2020-1-1 12:00)',
            'overview': '概要'
        }        

class UIForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('mailaddress',)
        labels = {
            'mailaddress': 'メールアドレス'
        }
