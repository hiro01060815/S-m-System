from django import forms
from .models import CoursesTaken,UserCTInfo, KadaiInfo, UserKadaiInfo, TestInfo, UserTestInfo,UserInfo
from .models import BaitoInfo, BaitoTimeInfo
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

class BIForm(forms.ModelForm):
    class Meta:
        model = BaitoInfo
        fields = ('name','base','plus_evening','plus_night','plus_holiday','plus_overtime')
        labels = {
            'name': 'バイト先',
            'base':'基本給（円）',
            'plus_evening':'夕方手当（円）',
            'plus_night':'深夜割増（％）',
            'plus_holiday':'祝日手当（円）',
            'plus_overtime':'8時間労働時の残業割増（％）'
        }


class BTIForm(forms.ModelForm):
    class Meta:
        model = BaitoTimeInfo
        fields = ('BI','in_time','out_time')
        labels = {
            'BI': 'バイト先の名前',
            'in_time':'出勤時間',
            'out_time':'退勤時間'            
        }
