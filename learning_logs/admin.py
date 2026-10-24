from django.contrib import admin

# Register your models here.
from .models import Topic     # 在本目录的model文件中导入Topic
from .models import Entry     # 导入条目entry

admin.site.register(Topic)    # 通过管理网站管理模型,注册主题
admin.site.register(Entry)    # 注册条目