from django import forms            # 导入表单模块
from .models import Topic,Entry     # 导入Topic Entry
class TopicForm(forms.ModelForm):   # Django的ModelForm是用于创建表单的工具.
    class Meta:                     # Meta 内部类，用于给外部类提供配置信息
        model = Topic               # 告诉Django 这个表单是有Topic这个数据库模型自动生成的
        fields = [ 'text' ]         # 指定字段：内容（不含date_added）
        labels = {'text':''}        # 标签为topic.text,但不显示。

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

