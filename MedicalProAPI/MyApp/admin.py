from django.contrib import admin
from .models import User,Tips, Friend, Emergency, Video, Coach, Hospital, Payment

admin.site.register(User)
admin.site.register(Tips)
admin.site.register(Friend)
admin.site.register(Emergency)
admin.site.register(Video)
admin.site.register(Coach)
admin.site.register(Hospital)
admin.site.register(Payment)