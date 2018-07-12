# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from LogsParse.libs.data import SSHClient
import datetime


def index(request):
    return render(request, 'index.html')


def data(request):
    url = request.GET.get('url')
    ip = request.GET.get('ip')
    pwd = request.GET.get('pwd')
    port = request.GET.get('port')
    client = SSHClient(host=ip, pwd=pwd, port=port)
    print('host = %s,url = %s,pwd = %s,port = %s' % (ip, url, pwd, port))
    SSH = client.ssh_connect()
    print('url=%s' % url)
    spider_num, logs_num = client.spider_number(SSH, url=url)
    num = len(logs_num)
    data = {"baidu": spider_num[0:num], "shenma": spider_num[num:num*2], "s360": spider_num[num*2:num*3], "shougou": spider_num[num*3:num*4], "category": logs_num}
    print(data)
    print('success')
    SSH.close()
    return HttpResponse(json.dumps(data, ensure_ascii=False))
