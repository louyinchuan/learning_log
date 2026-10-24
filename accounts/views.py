from django.shortcuts import render,redirect
from django.contrib.auth import login    # 用于让用户注册成功后就进入登陆状态
from django.contrib.auth.forms import UserCreationForm    # 用来早表格

# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # 有效则保存并登陆
            new_user = form.save()     # 先计算右边，密码按哈希值，再赋值给新用户
            login(request, new_user)   # 让新用户登陆
            return redirect('learning_logs:index')  # 跳转到主页

    # 如果没有进入else,还没填或者不合法
    context = {'form':form}
    return render(request, 'registration/register.html', context)



