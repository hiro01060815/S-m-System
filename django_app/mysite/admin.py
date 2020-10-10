from django.contrib import admin

from mysite.models import CoursesTaken,Post,UserCTInfo, UserKadaiInfo, KadaiInfo, UserInfo

admin.site.register(CoursesTaken)
admin.site.register(Post)
admin.site.register(UserCTInfo)
admin.site.register(KadaiInfo)
admin.site.register(UserKadaiInfo)
admin.site.register(UserInfo)