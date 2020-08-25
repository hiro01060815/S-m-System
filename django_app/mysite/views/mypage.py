from django.shortcuts import render
from mysite.models import CoursesTaken
from django.db.models import *
from django.contrib.auth.decorators import login_required

@login_required
def mypage_main(request):

    def get_CT_info(request):#時間割作成
        
        user = request.user
        data = CoursesTaken.objects.filter(user_id=user.id)
        period = data.period
        name = data.name
        school_credit = data.school_credit
        if data.filter(CT_status = 11).exists():
            sun = data.filter(CT_status = 11)
        else: 
            sun = " "
        
        mon = data.filter(CT_status = 12)
        tue = data.filter(CT_status = 13)
        wen = data.filter(CT_status = 14)
        thir = data.filter(CT_status = 15)
        fri = data.filter(CT_status = 16)
        stur = data.filter(CT_status = 17)
        
        params = {
            'sun':sun,
            'mon':mon,
            'tue':tue,
            'wen':wen,
            'thir':thir,
            'fri':fri,
            'stur':stur,
            'period':period,
            'name':name,
            'school_credit':school_credit,

        }
        return render(request, 'mypage.html', params)
