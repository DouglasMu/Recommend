import random

from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Userinfo, goods


def login(request):
    if request.method == "POST":
        if 'log' in request.POST:
            uf = UserFormLogin(request.POST)
            if uf.is_valid():
                # 获取表单信息
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                userResult = Userinfo.objects.filter(username=username, password=password)
                if (len(userResult) > 0):
                    # return render_to_response('Mainpage.html', {'operation': "登录"})
                    return HttpResponseRedirect('/main')
                else:
                    return HttpResponse("该用户不存在")
        else:
            return HttpResponseRedirect('/register')
    else:
        if 'reg' in request.POST:
            return HttpResponseRedirect('/register')
        else:
            uf = UserFormLogin()

    return render_to_response("Userlogin.html", {'uf': uf})


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)

        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            filterResult = Userinfo.objects.filter(username=username)
            if len(filterResult) > 0:
                return render_to_response('Register.html', {"errors": "用户名已存在"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
                if (password2 != password1):
                    errors.append("两次输入的密码不一致!")
                    return render_to_response('Register.html', {'errors': errors})
                    # return HttpResponse('两次输入的密码不一致!,请重新输入密码')
                password = password2
                email = uf.cleaned_data['email']
                # 将表单写入数据库
                user = Userinfo.objects.create(username=username,
                                               password=password1,email=email)
                user.save()
                # 返回注册成功页面
                # return render_to_response('Success.html', {'username': username, 'operation': "注册"})
                # 跳转到登录
                return HttpResponseRedirect('/login')
    else:
        uf = UserForm()

    return render_to_response('Register.html', {'uf': uf})


def main(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            return render_to_response('select.html',{'keywords':keywords})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(goods.objects.count()), 100)
    for i in sample:
        if (goods.objects.all()[i].price is not "0") \
                and (goods.objects.all()[i].price is not "-1"):
            results.append(goods.objects.all()[i])
    dic = {'context':results,'uf': uf}
    return render_to_response("Mainpage.html",dic )


# def search(request):
#     render_to_response('select.html',{'keywords':keywords})


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')


class UserFormLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class SelectForm(forms.Form):
    keywords = forms.CharField(label='搜索内容', max_length=255)