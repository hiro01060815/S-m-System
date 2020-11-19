from mysite.models import BaitoInfo,  BaitoTimeInfo
from django.db.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from mysite.forms import BIForm, BTIForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from datetime import time
import datetime
import locale
import math

@login_required
def baito_main(request):
    user = request.user
    form = BTIForm()
    message = ""
    if request.method == 'POST':
        form = BTIForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.user = request.user
            form1.save()
            return redirect(to='/baito')        
        else:
            message = '再入力して下さい'
            form = form



    if BaitoTimeInfo.objects.filter(user_id = user.id).exists():
        baitosaki_datas = BaitoTimeInfo.objects.filter(user_id = user.id)
        
        """
        sum_jitsudou : 実働時間合計
        sum_yuu      : 夕方の合計
        sum_22       : 深夜10時以降の合計
        sum_sun      : 祝日の合計
        sum_zan      : 8時間以上労働時の残業時間合計
        """
        sum_jitsudou = 0.0
        sum_yuu = 0.0
        sum_22 = 0.0
        sum_sun = 0.0
        sum_zan = 0.0
        tmp_jitsudou_salary =0.0
        tmp_yuu_salary  =0.0
        tmp_22_salary  =0.0
        tmp_sun_salary =0.0
        tmp_zan_salary=0.0

        time_16 = time(16, 00, 00)   #16時
        time_22 = time(22, 00, 00)   #22時
        time_8  = time( 8, 00, 00)
        salary = {'salary1': 0}
        i = 1
        d = datetime.date.today()
        for baitosaki_data in baitosaki_datas:
            print("----------------------------------------------------------------------")            
            print(str(baitosaki_data.in_time)+"~"+str(baitosaki_data.out_time))


            tmp_jitsudou = 0
            tmp_yuu = 0
            tmp_22 = 0
            tmp_sun = 0
            tmp_zan = 0

            tmp_jitsudou_salary =0.0
            tmp_yuu_salary  =0.0
            tmp_22_salary  =0.0
            tmp_sun_salary =0.0
            tmp_zan_salary=0.0

            jitsudou_salary = baitosaki_data.BI.base
            yuu_salary      = baitosaki_data.BI.plus_evening
            a22_salary      = ( 1.0 + baitosaki_data.BI.plus_night / 100) * baitosaki_data.BI.base
            sun_salary      = baitosaki_data.BI.plus_holiday
            zan_salary      = baitosaki_data.BI.plus_overtime


            tmp_jitsudou = int((baitosaki_data.out_time - baitosaki_data.in_time).seconds) #実働時間
            tmp_jitsudou_hour = tmp_jitsudou // 3600
            tmp_jitsudou_minute = (tmp_jitsudou - 3600*tmp_jitsudou_hour) // 60
            tmp_jitsudou_second = (tmp_jitsudou - 3600*tmp_jitsudou_hour - 60*tmp_jitsudou_minute)
            tmp_jitsudou_salary = jitsudou_salary * (tmp_jitsudou_hour + tmp_jitsudou_minute/60) 
            print("実働="+str(tmp_jitsudou_salary))

            
            if baitosaki_data.out_time.time() > time_16:                    #夕方の時間
                if baitosaki_data.in_time.time() < time_16 :
                    out_yuu = baitosaki_data.out_time.time()
                    tmp_yuu = int((datetime.datetime.combine(d, out_yuu) - datetime.datetime.combine(d, time_16)).seconds)
                    
                else:
                    tmp_yuu = int((baitosaki_data.out_time - baitosaki_data.in_time).seconds)
                tmp_yuu_hour = tmp_yuu // 3600
                tmp_yuu_minute = (tmp_yuu - 3600*tmp_yuu_hour) // 60
                tmp_yuu_second = (tmp_yuu - 3600*tmp_yuu_hour - 60*tmp_yuu_minute)
                tmp_yuu_salary = yuu_salary * (tmp_yuu_hour + tmp_yuu_minute/60) 
                print("夕方=" + str(tmp_yuu_salary))

            if baitosaki_data.out_time.time() > time_22:                    #深夜時間
                if baitosaki_data.in_time.time() < time_22:
                    out_22 = baitosaki_data.out_time.time()
                    tmp_22 = int((datetime.datetime.combine(d, out_22) - datetime.datetime.combine(d, time_22)).seconds)
                    
                else:
                    tmp_22 = int((baitosaki_data.out_time - baitosaki_data.in_time).seconds)
                tmp_22_hour = tmp_22 // 3600
                tmp_22_minute = (tmp_22 - 3600*tmp_22_hour) // 60
                tmp_22_second = (tmp_22 - 3600*tmp_22_hour - 60*tmp_22_minute)
                tmp_22_salary = a22_salary * (tmp_22_hour + tmp_22_minute/60) 
                print("深夜=" + str(tmp_22_salary))


            if baitosaki_data.holiday == 1:                                 #日祝
                tmp_sun = int((baitosaki_data.out_time - baitosaki_data.in_time).seconds)
                tmp_sun_hour = tmp_sun // 3600
                tmp_sun_minute = (tmp_sun - 3600*tmp_sun_hour) // 60
                tmp_sun_second = (tmp_sun - 3600*tmp_sun_hour - 60*tmp_sun_minute)
                tmp_sun_salary = sun_salary * (tmp_sun_hour + tmp_sun_minute/60) 
                print("祝日"+ str(tmp_sun_salary))
            
            a = int((baitosaki_data.out_time - baitosaki_data.in_time).seconds)
            a_hour = a // 3600
            a_minute = (a - 3600*a_hour) // 60
            a_second = (a - 3600*a_hour - 60*a_minute)
            

            if a_hour >= 8.0:                                                 #8時間以上の時の残業時間
                out_zan = baitosaki_data.out_time.time()
                in_zan = baitosaki_data.in_time.time()
                tmp_zan = int(( datetime.datetime.combine(d, out_zan) - datetime.datetime.combine(d, out_22)).seconds)
                tmp_zan_hour = tmp_zan // 3600
                tmp_zan_minute = (tmp_zan - 3600*tmp_zan_hour) // 60
                tmp_zan_second = (tmp_zan - 3600*tmp_zan_hour - 60*tmp_zan_minute)
                tmp_zan_salary = zan_salary * (tmp_zan_hour + tmp_zan_minute/60) 
                print("残業"+ str(tmp_zan_salary))

            tmp_salary = int(tmp_jitsudou_salary + tmp_yuu_salary + tmp_22_salary + tmp_sun_salary + tmp_zan_salary )
            print(str(baitosaki_data.in_time.date()) + "の給料" + str(tmp_salary))
            baitosaki_data.tmp_salary = tmp_salary

            aaa = "salary" + str(i)
            i = i + 1
            salary[aaa] = tmp_salary

            sum_jitsudou = sum_jitsudou + tmp_jitsudou
            sum_yuu = sum_yuu + tmp_yuu
            sum_22 = sum_22 + tmp_22
            sum_sun = sum_sun +tmp_sun
            sum_zan = sum_zan + tmp_zan
        
        sum_jitsudou_hour = sum_jitsudou // 3600
        sum_jitsudou_minute = (sum_jitsudou - 3600*sum_jitsudou_hour) // 60
        sum_jitsudou_second = (sum_jitsudou - 3600*sum_jitsudou_hour - 60*sum_jitsudou_minute)
        sum_jitsudou_salary = jitsudou_salary * (sum_jitsudou_hour + sum_jitsudou_minute/60) 

        sum_yuu_hour = sum_yuu // 3600
        sum_yuu_minute = (sum_yuu - 3600*sum_yuu_hour) // 60
        sum_yuu_second = (sum_yuu - 3600*sum_yuu_hour - 60*sum_yuu_minute)
        sum_yuu_salary = yuu_salary * (sum_yuu_hour + sum_yuu_minute/60) 

        sum_22_hour = sum_22 // 3600
        sum_22_minute = (sum_22 - 3600*sum_22_hour) // 60
        sum_22_second = (sum_22 - 3600*sum_22_hour - 60*sum_22_minute)
        sum_22_salary = a22_salary * (sum_22_hour + sum_22_minute/60) 

        sum_sun_hour = sum_sun // 3600
        sum_sun_minute = (sum_sun - 3600*sum_sun_hour) // 60
        sum_sun_second = (sum_sun - 3600*sum_sun_hour - 60*sum_sun_minute)
        sum_sun_salary = sun_salary * (sum_sun_hour + sum_sun_minute/60) 

        sum_zan_hour = sum_zan // 3600
        sum_zan_minute = (sum_zan - 3600*sum_zan_hour) // 60
        sum_zan_second = (sum_zan - 3600*sum_zan_hour - 60*sum_zan_minute)
        sum_zan_salary = zan_salary * (sum_zan_hour + sum_zan_minute/60)

        sum_salary = math.ceil(sum_jitsudou_salary) + math.ceil(sum_yuu_salary) + math.ceil(sum_22_salary) + math.ceil(sum_sun_salary) + math.ceil(sum_zan_salary) 
        #print(baitosaki_datas.values())
        #print(salary)

    params ={
        'message':message,
        'form': form,
        'baitosaki_datas': baitosaki_datas,
        'sum_salary': sum_salary,
        'salary_datas': salary

    }
    return render(request,'baito/baito_main.html',params)

def new_baito(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = BIForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to='/baito')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = BIForm()
    return render(request, 'baito/new_baito.html', params)      
    