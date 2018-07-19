# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from LogsParse.libs.data import SSHClient
from subprocess import PIPE, Popen
import datetime
import os

ssh_data = {
    '1': {'host': '142.234.162.99', 'port': 22, 'pwd': 'free@0516'},
    '2': {'host': '209.58.128.89', 'port': 22, 'pwd': 'E6zJ01V7Ykig'},
    '3': {'host': '198.56.192.250', 'port': 22, 'pwd': 'snow1029'},
    '4': {'host': '104.243.140.166', 'port': 22, 'pwd': 'Ptyw1q2w3e$R'},
    '5': {'host': '142.234.255.29', 'port': 22, 'pwd': 'AzVWuhQa1773'},
    '6': {'host': '45.34.107.130', 'port': 22, 'pwd': 'free0714'},
    '7': {'host': '45.42.95.170', 'port': 22, 'pwd': 'Ptyw1q2w3e$R'},
    '8': {'host': '142.234.162.79', 'port': 22, 'pwd': 'Vfc4RV1C01oy'},
    '9': {'host': '23.110.211.170', 'port': 22, 'pwd': 'Ptyw1q2w3e$R'},
    '10': {'host': '23.80.91.154', 'port': 22, 'pwd': 'free0514'},
}


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


def search_dir(request):
    group = request.GET.get('group')
    path = os.path.abspath('.')
    data = dict()
    if group == '9':
        dir = os.listdir('%s/LogsParse/domain' % path)
        for file in dir:
            urls = []
            domain = open('%s/LogsParse/domain/%s/domain.txt' % (path, file), 'r+')
            for line in domain:
                urls.append(line.strip('\n'))
            data[file] = urls
    return HttpResponse(json.dumps(data))


def search_url(request):
    url = request.GET.get('spider_url')
    dates = os.listdir('/www/wwwroot/xbw/temp/robotlog/Baiduspider/')
    category = []
    for date in dates:
        category.append(date.strip('.log').replace('2018', ''))
    category.sort()
    print(category)
    Baidu = spider_num('Baiduspider',category, str(url).split(' ')[2])
    result = dict()
    result['title'] = '九组蜘蛛池 域名：%s' % url
    result['category'] = category
    result['Baiduspider'] = Baidu
    result['Yisouspider'] = ['']
    result['360Spider'] = ['']
    result['sougou'] = ['']
    return HttpResponse(json.dumps(result))


def spider_num(spider_name, category, url):
    number = []
    for date in category:
        order = 'cat /www/wwwroot/xbw/temp/robotlog/%s/2018%s.log |grep %s|wc -l' % (spider_name, date, url.replace('http://'))
        print(order)
        pi = Popen(order, shell=True, stdout=PIPE)
        result = int(pi.stdout.read())
        number.append(result)
    return number