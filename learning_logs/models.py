'''
1、django 项目下包括（虚拟环境ll_env,总管manage/py,数据库db.sqligh3,总控室ll_project.learning_logs为新建项目名字）
2、learning_logs 是环境搭建好之后通过manage.py startapp learning_logs建立的项目，文件夹自动建立多个py文件
3、learning_logs 中包括models:为模型数据，和数据库打交道；views为视图负责交互？
'''
# 此文件旨在告诉Django如何处理应用程序中储存的数据

from django.db import models
from django.contrib.auth.models import User  # 引入用户，用来作为主题的外键

# 主题的类
class Topic(models.Model):      # 创建一个model的子类‘主题’，在Django中，一个类就是一张表。已经初始化了。
    # 用户学习主题 #
    owner = models.ForeignKey(User,on_delete=models.CASCADE)  # 为主题设置外键，并设置级联删除
    text = models.TextField(max_length=200)   # models.TextField 为短字符串类型，200长度够了
    date_added = models.DateTimeField(auto_now_add=True)  # 添加时间为动作时间
    def __str__(self):
        # 返回模型的字符串表⽰ #
        return self.text

# 条目的类
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)  # 为条目topic,设置user外键，并设置级联删除
    text = models.TextField()   #不限制长度
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "entries"   #多个条目时，显示正确的复数形式，而不是加-s
    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]} ... '   # 仅显示前50个字符
        else:
            return f'{self.text} '