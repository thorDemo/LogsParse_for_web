# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from LogsParse.libs.data import SSHClient
import datetime


def index(request):
    return render(request, 'index.html')


def data(request):
    client = SSHClient()
    SSH = client.ssh_connect()
    spider_num, logs_num = client.spider_number(SSH, url='aidshe.com')
    num = len(logs_num)
    data = {"baidu": spider_num[0:num], "shenma": spider_num[num:num*2], "s360": spider_num[num*2:num*3], "shougou": spider_num[num*3:num*4], "category": logs_num}
    print(data)
    print('请求成功')
    SSH.close()
    return HttpResponse(json.dumps(data, ensure_ascii=False))
