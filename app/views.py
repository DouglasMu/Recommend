import json
import random
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Userinfo, goods,pad,netbook
from spider.search import phone_search


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
                    return HttpResponseRedirect('/index')
                else:
                    # return HttpResponseRedirect('/login',{"status":"用户名密码错误"})
                    return render_to_response('Userlogin.html')
        else:
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
                if password2 != password1:
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
            select_list  = phone_search.search1(keywords)
            return render_to_response('select.html',{'select_list':select_list})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(goods.objects.count()), 500)
    for i in sample:
        if (goods.objects.all()[i].price is not "0") \
                and (goods.objects.all()[i].price != "-1") and\
                (int(goods.objects.all()[i].comment_num)>10000):
            results.append(goods.objects.all()[i])
    dic = {'context':results,'uf': uf}
    return render_to_response("tables.html",dic )


# def search(request):
#     render_to_response('select.html',{'keywords':keywords})

def feature(request):
    if request.method == "POST":
        goods_id = request.POST.get('id')
        with open("F:\\PythonFile\\Recommend\\app\\spider\\data\\feat.txt") as f:
            cont = f.read()
        dic_all = eval(cont)
        print(goods_id)
        feature_list = dic_all[goods_id]
        print(feature_list)
        listx = []
        listy = []
        dic = {}
        color = []
        for i in feature_list:
            y = (float((i[1]))-0.5)*2
            # listy.append(y)
            listx.append(i[0])
            if y >0:
                # color.append('green')
                listy.append(y)
            else:
                # color.append('red')
                dic['value'] = y
                dic['label'] = "labelRight"
                listy.append(dic)
        return render(request, "Feature.html",
                      {'x': json.dumps(listx), 'y': json.dumps(listy)})
        # return render(request, "feature.html", {'feature':feature_list})
        # return render_to_response("Feature.html",{'feature':feature_list})



class UserForm(forms.Form):
    username = forms.CharField(label=' 用户账号 ', max_length=100)
    password1 = forms.CharField(label=' 用户密码 ', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')


class UserFormLogin(forms.Form):
    username = forms.CharField(label='账号', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class SelectForm(forms.Form):
    keywords = forms.CharField(label='',max_length=255)


def index(request):
    return render_to_response('index.html')


def charts(request):
    listx = []
    listx.append(int(goods.objects.count()))
    listx.append(int(pad.objects.count()))
    listx.append(int(netbook.objects.count()))
    # listx = [1900,2000,2000]
    listy = ['手机','平板','笔记本']
    return render(request, "charts.html",
                  {'x':json.dumps(listx),'y':json.dumps(listy)})


def test(request):
    return render_to_response('tables.html')


def phone(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            select_list  = phone_search.search1(keywords)
            return render_to_response('select.html',{'select_list':select_list})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(goods.objects.count()), 500)
    for i in sample:
        if (goods.objects.all()[i].price is not "0") \
                and (goods.objects.all()[i].price is not "-1") \
                and (int(goods.objects.all()[i].comment_num)>10000):
            results.append(goods.objects.all()[i])
    dic = {'context':results,'uf': uf}
    return render_to_response("tables.html",dic )


def netbook_m(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            select_list  = phone_search.search1(keywords)
            return render_to_response('select.html',{'select_list':select_list})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(netbook.objects.count()), 500)
    for i in sample:
        if (netbook.objects.all()[i].price is not "0") \
                and (netbook.objects.all()[i].price is not "-1")\
                and (int(netbook.objects.all()[i].comment_num)>10000):
            results.append(netbook.objects.all()[i])
    dic = {'context':results,'uf': uf}
    return render_to_response("tables.html",dic )


def pad_m(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            select_list  = phone_search.search1(keywords)
            return render_to_response('select.html',{'select_list':select_list})
    else:
        uf = SelectForm()
    results = []

    sample = random.sample(range(pad.objects.count()), 500)
    for i in sample:
        if (pad.objects.all()[i].price is not "0") \
                and (pad.objects.all()[i].price is not "-1")\
                and (int(pad.objects.all()[i].comment_num)>10000):
            results.append(pad.objects.all()[i])
    dic = {'context':results,'uf': uf}
    return render_to_response("tables.html",dic )


def netbooksearch(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            select_list = phone_search.search1(keywords)
            return render_to_response('select.html', {'select_list': select_list})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(goods.objects.count()), 50)
    for i in sample:
        if (goods.objects.all()[i].price is not "0") \
                and (goods.objects.all()[i].price is not "-1"):
            results.append(goods.objects.all()[i])
    dic = {'context': results, 'uf': uf}
    return render_to_response("tables.html", dic)



def phonesearch(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            select_list = phone_search.search1(keywords)
            return render_to_response('select.html', {'select_list': select_list})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(goods.objects.count()), 50)
    for i in sample:
        if (goods.objects.all()[i].price is not "0") \
                and (goods.objects.all()[i].price is not "-1")and\
                     (int(goods.objects.all()[i].comment_num)>10000):
            results.append(goods.objects.all()[i])
    dic = {'context': results, 'uf': uf}
    return render_to_response("tables.html", dic)


def padsearch(request):
    if request.method == "POST":
        uf = SelectForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            keywords = uf.cleaned_data['keywords']
            print(keywords)
            select_list = phone_search.search1(keywords)
            return render_to_response('select.html', {'select_list': select_list})
    else:
        uf = SelectForm()
    results = []
    sample = random.sample(range(goods.objects.count()), 50)
    for i in sample:
        if (goods.objects.all()[i].price is not "0") \
                and (goods.objects.all()[i].price is not "-1"):
            results.append(goods.objects.all()[i])
    dic = {'context': results, 'uf': uf}
    return render_to_response("tables.html", dic)