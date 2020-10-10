from django.urls import path
 
from .views import views
from .views import mypage,kadai_test_plus, mail
 
# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'mysite'
 
urlpatterns = [
    path('', views.index, name='home'),
    path('mypage',mypage.mypage_main,name='mypage'),
    path('new_CT',mypage.new_CT,name='new_CT'),
    path('CT_overview/<int:pk>',mypage.CT_overview,name='CT_overview'),
    path('CT_update/<int:pk>',mypage.CT_update, name='CT_update'),
    path('CT_info/<int:pk>',mypage.CT_info, name = 'CT_info'),
    path('k_t_p', kadai_test_plus.k_t_p_main, name = 'k_t_p'),
    path('kadai/<int:pk>',kadai_test_plus.kadai,name='kadai'),
    path('kadai_update/<int:pk>', kadai_test_plus.kadai_update, name='kadai_update'),
    path('kadai_delete/<int:pk>', kadai_test_plus.kadai_delete, name='kadai_delete'),
    #path('k_t_p',kadai_test_plus.kadai_status_update, name = 'kadai_status_update'),
    path('regi_mail', mail.mail_touroku, name ='regi_mail'),
    path('update_mail', mail.mail_update, name = 'update_mail'),
    path('mail_check', mail.mail_check, name = 'mail_check')
]