from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import BadHeaderError, send_mail
from mysite.models import CoursesTaken, UserCTInfo, KadaiInfo, UserKadaiInfo, UserInfo
import datetime
import schedule
import time
from mysite.forms import UIForm
import sched, time, datetime

def mail(request):
    print("run")
    user = request.user
    kadai_datas = UserKadaiInfo.objects.filter(user_id = user.id)
    kadai_datas = kadai_datas.filter(status = 0)
    dt_now = datetime.datetime.now()
    d_now = dt_now.date()
    d_plus3 = d_now + datetime.timedelta(days=3)
    message = ""
    for kadai_data in kadai_datas:
        kadai_date = kadai_data.KI.date.date()
        if (kadai_date <= d_plus3 and kadai_date >= d_now):
            message += str(kadai_data.KI.name) + "( " + "http://127.0.0.1:8000/kadai/" + str(kadai_data.id) + " )\n"

    """題名"""
    subject = "期限が間近の課題、テストがあります。"
    """本文"""
    print(message)
    message = "期限が3日以内の課題があります。確認してください。\n" + message +"\n\n\nhttp://127.0.0.1:8000/"
    """送信元メールアドレス"""
    from_email = "s.m.system.info@gmail.com"
    """宛先メールアドレス"""
    obj = UserInfo.objects.get(user_id = user.id)
    mail = str(obj.mailaddress)
    recipient_list = [
        mail
    ]

    send_mail(subject, message, from_email, recipient_list)





 

def mail_check(request): #本人確認
    user = request.user
    obj = UserInfo.objects.get(user_id = user.id)
    """
    obj = UserInfo(user = user,address_status = 2)
    obj.save()
    """
    obj.address_status = 2
    obj.save()
    params = {
        'user':user
    }
    return render(request, 'mypage/mail_check.html', params)


def check_send_mail(mail,user): #仮登録メール
    subject = "メールの本登録をお願いします。"
    """本文"""
    message = user+"さん下記urlからメールの本登録をお願いします。\nこのメールに身に覚えのない場合はアクセスしないでください。\n\
        本登録url( http://127.0.0.1:8000/mail_check )"
    """送信元メールアドレス"""
    from_email = "s.m.system.info@gmail.com"
    """宛先メールアドレス"""
    recipient_list = [
        mail
    ]

    send_mail(subject, message, from_email, recipient_list)


def mail_touroku(request): #メアド新規登録
    a = 0
    params = {'message': '', 'form': None, 'a':a,}
    if request.method == 'POST':
        form = UIForm(request.POST)
        if form.is_valid():
            #form.save()
            #print(form.save().id)
            #print(form.save())
            user_id = request.user
            mail = request.POST['mailaddress']
            UserInfo(user = user_id,mailaddress = mail, address_status = 1).save()
            check_send_mail(str(mail),str(user_id))
            return redirect(to='/mypage')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
            params['a'] = a
    else:
        params['form'] = UIForm()
        params['a'] = a
    return render(request, 'mypage/mail.html', params)  
    
def mail_update(request): #メアド更新
    a = 1
    user = request.user
    obj = UserInfo.objects.get(user_id = user.id)
    #obj = obj.mailaddress
    #print(obj)
    if(request.method == 'POST'):
        update_info = UIForm(request.POST, instance = obj)
        update_info.save()

        obj.address_status = 1
        obj.save()
        mail = request.POST['mailaddress']
        check_send_mail(str(mail),str(user))
        return redirect('mysite:mypage')
        
    params = {
        'form': UIForm(instance = obj),
        'a':a,
    }
    return render(request,'mypage/mail.html',params)