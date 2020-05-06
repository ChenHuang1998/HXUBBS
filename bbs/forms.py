from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from bbs.models import UserProfile, Post
from ckeditor_uploader.fields import RichTextUploadingFormField, RichTextUploadingField
from ckeditor.widgets import CKEditorWidget


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-material', 'placeholder': '请输入用户名'}),error_messages={'required':'不能为空'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-material', 'placeholder': '密码'}),error_messages={'required':'不能为空'})

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class RegForm(forms.Form):
    username = forms.CharField(max_length=16,
                               min_length=3,
                               widget=forms.TextInput(
                                   attrs={'class': 'input-material', 'placeholder': '请输入3-16位的用户名'}))
    password = forms.CharField(min_length=6,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input-material', 'placeholder': '请输入密码'}))
    password_again = forms.CharField(min_length=6,
                                     widget=forms.PasswordInput(
                                         attrs={'class': 'input-material', 'placeholder': '再输入一次密码'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次密码不一致')
        if password == '12345678':
            raise forms.ValidationError('密码过于简单')
        return password_again


class PublishForm(forms.Form):
    content = RichTextUploadingFormField(label='', config_name='publish', error_messages={'required': '内容不能为空'})
