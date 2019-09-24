from django import forms
from .models import Topci, Entry

class TopicForm(forms.ModelForm):
    """定义一个TopicForm类 继承了forms.ModelForm"""
    class Meta:
        """嵌套一个Meta类（这是最简单的ModelForm版本）"""
        model = Topci
        # 表单中只包含字段text
        fields = ['text']
        # 让Django不要为字段text生成标签
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 文本域的宽度设为80
        widgets = {'text':forms.Textarea(attrs={'cols':80})}