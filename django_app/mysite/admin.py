from django.contrib import admin

from mysite.models import CoursesTaken,Post,UserCTInfo, UserKadaiInfo, KadaiInfo, UserInfo,BaitoTimeInfo,BaitoInfo

admin.site.register(CoursesTaken)
admin.site.register(Post)
admin.site.register(UserCTInfo)
admin.site.register(KadaiInfo)
admin.site.register(UserKadaiInfo)
admin.site.register(UserInfo)
admin.site.register(BaitoInfo)
admin.site.register(BaitoTimeInfo)