from django.shortcuts import render
from django.http import HttpResponse
import datetime
from mysite.models import UserKadaiInfo, UserInfo
from mysite.views.mail import mail
import threading
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
                    mail(request)
    kadai_datas = UserKadaiInfo.objects.filter(user_id = user.id)
    if kadai_datas.filter(status = 1).exists():
        dt_now = datetime.datetime.now()
        d_now = dt_now.date()
        d_minus7 = d_now + datetime.timedelta(days=-7)
        submit_kadai_datas = kadai_datas.filter(KI__submit_date__range=[d_minus7, d_now])
    params = {
        'submit_kadai_datas':submit_kadai_datas,
    }


    return render(request,'index.html',params)


