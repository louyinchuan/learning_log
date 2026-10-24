from django import forms            # 导入表单模块
from .models import Topic,Entry     # 导入Topic Entry
class TopicForm(forms.ModelForm):   # Django的ModelForm是用于创建表单的工具.
    class Meta:                     # Meta 内部类，用于给外部类提供配置信息
        model = Topic               # 告诉Django 这个表单是有Topic这个数据库模型自动生成的
        fields = [ 'text' ]         # 指定字段：内容（不含date_added）
        labels = {'text':''}        # 标签为topic.text,但不显示。

    # 👇 新增这个方法，用来校验 text 字段...下面这段是用来避免输入重复主题
    def clean_text(self):
        # 1. 先拿到用户输入的数据（注意：这里不要加 .strip()，先原样拿出来）
        text = self.cleaned_data['text']
        # 2. 去数据库里查，看看是不是已经有这个主题了（利用 iexact 忽略大小写）
        if Topic.objects.filter(text__iexact=text).exists():
            # 3. 如果有，抛出验证错误。！！！！！！！！！！此处待修改，是要验证用户名下有无同名主题
            raise forms.ValidationError("这个主题已经存在啦，换一个吧！")
        # 4. 如果没有，必须把数据 return 回去，否则表单拿不到数据
        return text

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={
            'cols':80,
            'rows':20,
            'style': 'width: 100%;'
        })} # 告诉浏览器，需要一个大的输入框，每行有80字符
