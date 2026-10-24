

from django.urls import path   # 映射路基需要path
from . import views            # 当前目录的view。view 是django中负责业务逻辑的地方：查数据库，生成网页HTML

'''
定义程序learning_logs的路由规则：
1、如果输入http://127.0.0.1:8000/，进入learning_logs.urls，执行views.index
'''

app_name = 'learning_logs'    # 给应用起名.注意‘app_name’是Django 的配置约定，不能改。
# 指定路由规则：
urlpatterns = [
    # 主页
    path('', views.index, name='index'),    # 若路径为http://127.0.0.1:8000/， 执行views.index。 页面名称为‘index’
    path('topics/', views.topics, name='topics'),   #路径为http://127.0.0.1:8000/topics. 执行views.topics网页名topics
    path('topics/<int:topic_id>/', views.topic, name='topic'), #路径后有主题id，转到相关主题
    path('new_topic/', views.new_topic, name='new_topic'),  # 新主题页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  #新条目页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  #条目修改页面
]