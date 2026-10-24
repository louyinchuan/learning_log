from django.urls import path, include  # 引入path include
from . import views
app_name = 'accounts'   # 命名空间
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # 把路由规则打包给django自带的用户处理模块,模块自带路由规则及视图，但网页模板还需要自己创建
    # django.contrib.auth.urls 管理登陆登出 不管理增减用户-注册及销户
    path('register/',views.register, name='register'),
]
