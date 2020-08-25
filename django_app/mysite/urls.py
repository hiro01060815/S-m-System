from django.urls import path
 
from .views import views
from .views import mypage
 
# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'mysite'
 
urlpatterns = [
    path('', views.index, name='index'),
    path('mypage',mypage.mypage_main,name='mypage')

]