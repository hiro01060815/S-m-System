from mysite.models import CoursesTaken, UserCTInfo, UserInfo, UserKadaiInfo
from django.db.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from mysite.forms import UserForm, UserForm1, KIForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@login_required
def mypage_main(request):

    def get_CT_info(request):#時間割作成
        
        user = request.user
        data = UserCTInfo.objects.filter(user_id = user.id)
        CT_data = data.filter(user_CT = 1)
        return CT_data

    user = request.user
    if UserInfo.objects.filter(user_id = user.id).exists():
        mail_status = UserInfo.objects.filter(user_id = user.id)
        address = mail_status

        CT_data=get_CT_info(request)
        status = 1
        monday_datas = CT_data.filter(CT__CT_status = 2)
        tuesday_datas = CT_data.filter(CT__CT_status = 3)
        wednesday_datas = CT_data.filter(CT__CT_status = 4)
        thursday_datas = CT_data.filter(CT__CT_status = 5)
        friday_datas = CT_data.filter(CT__CT_status = 6)
        saturday_datas = CT_data.filter(CT__CT_status = 7)
        params = {
            'CT_data':CT_data,
            'address': address,
            'status':status,
            'monday_datas':monday_datas,
            'tuesday_datas':tuesday_datas,
            'wednesday_datas':wednesday_datas,
            'thursday_datas':thursday_datas,
            'friday_datas':friday_datas,
            'saturday_datas':saturday_datas,
        }
        return render(request, 'mypage/mypage_main.html', params)
    else:
        status = 0
        CT_data=get_CT_info(request)
        address = ""
        monday_datas = CT_data.filter(CT__CT_status = 2)
        tuesday_datas = CT_data.filter(CT__CT_status = 3)
        wednesday_datas = CT_data.filter(CT__CT_status = 4)
        thursday_datas = CT_data.filter(CT__CT_status = 5)
        friday_datas = CT_data.filter(CT__CT_status = 6)
        saturday_datas = CT_data.filter(CT__CT_status = 7)
        params = {
            'CT_data':CT_data,
            'address': address,
            'status':status,
            'monday_datas':monday_datas,
            'tuesday_datas':tuesday_datas,
            'wednesday_datas':wednesday_datas,
            'thursday_datas':thursday_datas,
            'friday_datas':friday_datas,
            'saturday_datas':saturday_datas,
        }
        return render(request, 'mypage/mypage_main.html', params)



def new_CT(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user_id = request.user
            UserCTInfo(user = user_id,CT = form.save(), user_CT = 1).save()

            return redirect(to='/mypage')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'mypage/new_CT.html', params)   


def CT_overview(request,pk):
    CT_data = get_object_or_404(UserCTInfo,pk=pk)
    CT_name = CT_data.CT.name
    CT_youbi = CT_data.CT.CT_status
    CT_jigen = CT_data.CT.period
    CT_credit = CT_data.CT.school_credit
    CT_rishuujoutai = CT_data.user_CT
    CT_id = CT_data.id
    
    params = {
        'CT_name':CT_name,
        'CT_youbi':CT_youbi,
        'CT_jigen':CT_jigen,
        'CT_credit':CT_credit,
        'CT_rishuujoutai':CT_rishuujoutai,
        'CT_data':CT_data,
        'CT_id': CT_id
    }
    return render(request,'mypage/CT_overview.html',params) 

def CT_update(request,pk):
    obj = CoursesTaken.objects.get(id=pk)
    obj1 = UserCTInfo.objects.get(id=pk)
    id = pk  
    if(request.method == 'POST'):
        update_info = UserForm(request.POST, instance = obj)
        update_info1 = UserForm1(request.POST, instance = obj1)
        update_info.save()
        update_info1.save()
        return redirect('mysite:CT_info', pk=id)
    
    params = {
        'CT_id':pk,
        'form': UserForm(instance = obj),
        'form1': UserForm1(instance = obj1),
    }
    return render(request,'mypage/CT_update.html',params)

def CT_info(request,pk):
    user = request.user
    kadai_data = UserKadaiInfo.objects.filter(user_id = user.id) #ユーザごとの課題をフィルタ
    kadai_data = kadai_data.filter(KI__display = 0) #削除されていないデータを選択
    kadai_data = kadai_data.filter(KI__CT__pk = pk)
    kadai_data1 = kadai_data.filter(status = 0) #未提出
    kadai_data2 = kadai_data.filter(status = 1) #提出済
    CT_name = CoursesTaken.objects.get(pk = pk)
    if (request.method == 'POST'):
        KIform =  KIForm(request.POST)
        if KIform.is_valid():
            KIform.save()
            user_id = request.user
            UserKadaiInfo(user = user_id, KI = KIform.save(), status = 0).save()
            return redirect(to='/k_t_p')
        
        else:
            params = {
                'CT_name':CT_name,
                'kadai_data1':kadai_data1,
                'kadai_data2':kadai_data2,
                'KIform': KIForm(),
                'pk':pk,
            }    
    else:
        params = {
        'CT_name':CT_name,
        'kadai_data1':kadai_data1,
        'kadai_data2':kadai_data2,
        'KIform': KIForm(),
        'pk':pk,
        }
    params = {
        'CT_name':CT_name,
        'kadai_data1':kadai_data1,
        'kadai_data2':kadai_data2,
        'KIform': KIForm(),
        'pk':pk,
    }
    return render(request,'mypage/CT_info.html',params)
