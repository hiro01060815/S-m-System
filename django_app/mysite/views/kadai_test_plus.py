from mysite.models import CoursesTaken, UserCTInfo, KadaiInfo, UserKadaiInfo, UserTestInfo, TestInfo
from django.db.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from mysite.forms import KIForm, UKIForm, TIForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import datetime
def k_t_p_main(request):
    user = request.user
    kadai_data = UserKadaiInfo.objects.filter(user_id = user.id)
    kadai_data = kadai_data.filter(KI__display = 0)
    kadai_datas = kadai_data.filter(status = 0)
    #print(kadai_datas.order_by('KI__date'))
    kadai_datas.order_by('KI__date').first()
    test_data = UserTestInfo.objects.filter(user_id = user.id)
    test_datas = test_data.filter(status = 0)
    now = datetime.datetime.now()
    now_year = now.year
    now_month = now.month
    now_day = now.day + 3
    dt_now = datetime.datetime.now()
    d_now = dt_now.date()
    d_plus3 = d_now + datetime.timedelta(days=3)
    #print(str(len(kadai_datas)))  #辞書の長さを検証
    params = {
        'kadai_datas': kadai_datas,
        'test_datas': test_datas,
        'KIform': KIForm(),
        'TIform': TIForm(),
        'now_year': now_year,
        'now_month':now_month,
        'now_day': now_day,
    }
    if (request.method == 'POST'):
        if 'kadai_button' in request.POST:
            KIform =  KIForm(request.POST)
            if KIform.is_valid():
                KIform.save()
                user_id = request.user
                UserKadaiInfo(user = user_id, KI = KIform.save(), status = 0).save()
                return redirect(to='/k_t_p')
            
            else:
                params = {
            'kadai_datas': kadai_datas,
            'test_datas': test_datas,
            'KIform': KIForm(),
            'TIform': TIForm(),
            'now_year': str(now_year),
            'now_month':str(now_month),
            'now_day': str(now_day),
                }
        elif 'test_button' in request.POST:
            TIform =  TIForm(request.POST)
            if TIform.is_valid():
                TIform.save()
                user_id = request.user
                UserTestInfo(user = user_id, TI = TIform.save(), status = 0).save()
                return redirect(to='/k_t_p')
            
            else:
                params = {
            'kadai_datas': kadai_datas,
            'test_datas': test_datas,
            'KIform': KIForm(),
            'TIform': TIForm(),
            'now_year': now_year,
            'now_month':now_month,
            'now_day': now_day,
                    }
    else:
        params = {
        'kadai_datas': kadai_datas,
        'test_datas': test_datas,
        'KIform': KIForm(),
        'TIform': TIForm(),
        'now_year': now_year,
        'now_month':now_month,
        'now_day': now_day,
    }
        

    return render(request, 'kadai_test_plus/k-t-p_main.html', params)


def kadai(request,pk):

    obj = KadaiInfo.objects.get(id=pk)
    obj1 = UserKadaiInfo.objects.get(id=pk)
    CT_id = obj.CT.id

    
    
    params = {
        'obj':obj,
        'obj1':obj1,
        'kadai_id':pk,
        'CT_id':CT_id,
    }
    return render(request, 'kadai_test_plus/kadai.html', params)

def kadai_update(request, pk):
    obj = KadaiInfo.objects.get(id=pk)
    obj1 = UserKadaiInfo.objects.get(id=pk)
    id = pk  
    CT_id = obj.CT.id
    if(request.method == 'POST'):
        update_info = KIForm(request.POST, instance = obj)
        update_info1 = UKIForm(request.POST, instance = obj1)
        update_info.save()
        update_info1.save()
        if obj1.status == 1:
            dt_now = datetime.datetime.now()
            d_now = dt_now.date()
            obj.submit_date = d_now
            obj.save()
        moji = "更新しました"
        params = {
            'obj':obj,
            'obj1':obj1,
            'kadai_id':pk,
            'moji':moji,
            'CT_id':CT_id,
        }
        return render(request, 'kadai_test_plus/kadai.html', params)
    
    params = {
        'kadai_id':pk,
        'form': KIForm(instance = obj),
        'form1': UKIForm(instance = obj1),
    }
    return render(request,'kadai_test_plus/kadai_update.html',params)

def kadai_delete(request,pk):
    obj = KadaiInfo.objects.get(id=pk)
    obj1 = UserKadaiInfo.objects.get(id=pk)
    if (request.method == 'POST'):
        obj.display = 1
        obj.save()
        return redirect(to='/k_t_p')
    
    
    params = {
        'obj':obj,
        'obj1':obj1,
        'kadai_id':pk,
    }
    return render(request, 'kadai_test_plus/kadai_delete.html',params)


