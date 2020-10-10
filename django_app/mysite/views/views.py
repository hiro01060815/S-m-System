from django.shortcuts import render
from django.http import HttpResponse
import datetime
from mysite.models import UserKadaiInfo, UserInfo, UserCTInfo
from django.db.models import Sum
from mysite.views.mail import mail
import threading
from django.contrib.auth.decorators import login_required
import re

@login_required
def index(request):
    
    user = request.user
    if UserInfo.objects.filter(user_id = user.id).exists():
        obj = UserInfo.objects.get(user_id = user.id)
        if obj.address_status == 2:
            kadai_datas = UserKadaiInfo.objects.filter(user_id = user.id)
            kadai_datas = kadai_datas.filter(status = 0)
            dt_now = datetime.datetime.now()
            d_now = dt_now.date()
            d_plus3 = d_now + datetime.timedelta(days=3)
            for kadai_data in kadai_datas:
                kadai_date = kadai_data.KI.date.date()
                if (kadai_date <= d_plus3 and kadai_date >= d_now):
                    #mail(request)
                    print("z")
    kadai_datas = UserKadaiInfo.objects.filter(user_id = user.id)
    if kadai_datas.filter(status = 1).exists():    #提出した日が一週間以内の課題
        dt_now = datetime.datetime.now()
        d_now = dt_now.date()
        d_minus7 = d_now + datetime.timedelta(days=-7)
        submit_kadai_datas = kadai_datas.filter(KI__submit_date__range=[d_minus7, d_now])
    else:
        submit_kadai_datas = ""

    if UserCTInfo.objects.filter(user_id = user.id).exists(): #履修中の科目の総単位を計算
        CT_datas = UserCTInfo.objects.filter(user_id = user.id)
        CT_datas = CT_datas.filter(user_CT = 1)
        credit_sum = CT_datas.all().aggregate(Sum('CT__school_credit'))
        credit_sum = str(credit_sum)
        credit_sum = re.sub("\\D","",credit_sum)
    else:
        credit_sum = 0
    params = {
        'submit_kadai_datas':submit_kadai_datas,
        'credit_sum':credit_sum,
    }


    return render(request,'index.html',params)


