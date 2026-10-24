from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# 用于渲染网页视图,重定向。用于新主题添加成功后返回所有主题页面.get_object_or_404 用于对没有的数据返回404而非返回不存在
from django.http import Http404       # 导入404响应：当服务器没有被请求的资源时，标准做法是返回404
from .models import Topic,Entry      # 从当前目录的models 引入Topic
from .forms import TopicForm,EntryForm   # 从当前目录的forms 引入TopicForm



# Create your views here.

def index(request):    # request 是django传来的数据包，包含用户访问的信息
    return render(request,'learning_logs/index.html')   # 返回一个网页

@login_required   # django 自带，访问主题时，检查是否登陆，否则定义到LOGIN_URL,因此需要在设置中注明
# 定义views中指定的程序topics
def topics(request):
    # 定义要显示的内容，用于后面render
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # filter(owner=request.user) 过滤器，括号内为条件
    # 从数据库获取主题，并根据创建时间排序，返回列表
    context = {'topics': topics}   # 返回一个字典
    return render(request,'learning_logs/topics.html',context)

# 定义专门主题
@login_required
def topic(request, topic_id):
    # topic = Topic.objects.get(id=topic_id)
    # 这是教材代码，问题在于如果topic_id不存在，无法返回404,修改如下：
    topic = get_object_or_404(Topic,id=topic_id,owner=request.user)  #这里如果内容不存在，或用户无权返回404
    # if topic.owner != request.user:
        # raise Http404('此页面不存在，或您无权限访问。')
    entries = topic.entry_set.order_by('date_added')
    # 返回查询集。因为entry通过外键关联到topic，根据django，可用entry_set
    # topic.entry_set : 属于该主题的条目
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

# 新建主题页面。用户打开是，是get. 填入数据是post,因而要分情况做出反应，用if判断
# 输入的数据要判断是否is_valid(合法)，合法存入表单跳回主题集页避免重复添加，不合法渲染当前页面并指出错误
@login_required
def new_topic(request):
    # 判断用户的request类型为get还是post
    if request.method != 'POST':  # 没填数据，即刚打开页面
        form = TopicForm()        # 创建一个新表单
    else:
        form = TopicForm(data = request.POST)   # 为填入数据创建一个表单
        # 然后判断表单是否合法
        if form.is_valid():
            text = form.cleaned_data['text']
            # 主题查重
            if Topic.objects.filter(owner=request.user, text__iexact=text).exists():
                # 如果查到了，给表单塞个错误，不保存
                form.add_error('text', '你名下已经有同名的主题啦，换一个吧！')
            else:
                new_topic = form.save(commit=False) # 记住主题，暂不存入
                new_topic.owner = request.user      # 指定新主题的owner外键
                new_topic.save()
                return redirect('learning_logs:topics')    # 合法就保存并返回主题集页
    context = {'form': form}  # 把信息打包成字典，共render调用
    return render(request, 'learning_logs/new_topic.html', context) # 还在新建主题页渲染错误信息

@login_required
def new_entry(request,topic_id):
    topic = get_object_or_404(Topic,id=topic_id,owner=request.user)
    if request.method != 'POST':
        form = EntryForm
    else :
        form = EntryForm(data= request.POST)
        if form.is_valid():
            # 👇 【加在这里】检查这个主题下有没有相同的内容
            text = form.cleaned_data['text']
            if Entry.objects.filter(topic=topic, text=text).exists():
                form.add_error('text', '这个条目内容已经存在啦，不用再记一次！')
            else:
                new_entry = form.save(commit=False)  # 先不保存，也无法写入，还差主题外键
                new_entry.topic = topic  # 获取主题外键
                new_entry.save()   # 保存
                return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):  # 修改条目
    # entry = Entry.objects.get(id=entry_id)   #教材写法
    # topic = entry.topic                      #教材写法
    # if topic.owner != request.user:          #教材写法
    #    raise Http404                         #教材写法

    # 改写如下：注意topic__owner 注意是两个下划线。跨关系查找的专用分隔符
    entry = get_object_or_404(Entry, id=entry_id, topic__owner=request.user)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else :
        form = EntryForm(data = request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


