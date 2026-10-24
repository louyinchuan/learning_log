"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin   # 导入django的后台管理模块
from django.urls import path       # path函数处理网址与处理程序之间的关系
from django.urls import include    # django的 include 类似python的import，用于导入蒂塔应用的规则

'''
定义项目ll_project的路由规则：
1、如果输入http://127.0.0.1:8000/admin/，进入后台管理
2、如果输入http://127.0.0.1:8000/，进入learning_logs.urls
'''
urlpatterns = [                                    # 列表，定义网址路由规则，当有人访问网站时，django会依次检查列表，扎到匹配的路径。
    path('admin/', admin.site.urls),         # 如果地址输入admin/ 则后续请求交给Django后台管理系统
    path('accounts/', include('accounts.urls')),
    path('',include('learning_logs.urls')),
]
     # 如果输入根路径http://127.0.0.1:8000/，跳转倒learning_logs.urls]
