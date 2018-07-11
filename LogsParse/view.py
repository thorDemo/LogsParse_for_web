# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from LogsParse.lib.data import SSHClient
import datetime


def index(request):
    context = dict()
    context['hello'] = '老子吃火锅你吃火锅底料'
    return render(request, 'index.html', context)


def data(request):
    client = SSHClient()
    SSH = client.ssh_connect()
    temp = client.spider_number(SSH, url='ctcban.com')
    date = datetime.datetime.now().strftime('%Y%m%d')
    category = []
    for day in range(0, 10):
        this_day = (datetime.datetime.strptime(date, '%Y%m%d') - datetime.timedelta(days=(10 - day))).strftime('%Y%m%d')
        category.append(this_day)
    data = {"baidu": temp[0:10], "shenma": temp[10:20], "s360": temp[20:30], "shougou": temp[30:40], "category":category}
    print('请求成功')
    SSH.close()
    return HttpResponse(json.dumps(data, ensure_ascii=False))
