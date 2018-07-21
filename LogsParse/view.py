# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from LogsParse.libs.data import SSHClient
from subprocess import PIPE, Popen
import datetime
import os
from LogsParse.tools.search_group import insert_spider_group_url

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


# 刷新数据库
def refresh_data(request):
    group_id = request.GET.get('group_id')
    subtext = request.GET.get('subtext')
    url = str(subtext).split('//', 2)[1]
    try:
        insert_spider_group_url(group_id, url)
    except Exception as e:
        return HttpResponse(json.dumps({'message': 'exception %s' % url}))
    return HttpResponse(json.dumps({'message': 'this is group %s' % group_id}))


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
    else:
        data['message'] = 'this is group %s' % group
    return HttpResponse(json.dumps(data))


def search_url(request):
    url = str(request.GET.get('spider_url')).split(' ')[2]
    dates = os.listdir('/www/wwwroot/xbw/temp/robotlog/Baiduspider/')
    category = []
    for date in dates:
        category.append(date.strip('.log').replace('2018', ''))
    category.sort()
    print(category)
    Baidu = spider_num('Baiduspider',category, url)
    Yisouspider = spider_num('Yisouspider', category, url)
    Spider360 = spider_num('360Spider', category, url)
    sogou = spider_num('sogou', category, url)
    result = dict()
    result['title'] = '九组蜘蛛池 域名：%s' % url
    result['category'] = category
    result['Baiduspider'] = Baidu
    result['Yisouspider'] = Yisouspider
    result['360Spider'] = Spider360
    result['sogou'] = sogou
    return HttpResponse(json.dumps(result))


def spider_num(spider_name, category, url):
    number = []
    for date in category:
        order = 'cat /www/wwwroot/xbw/temp/robotlog/%s/2018%s.log |grep %s|wc -l' % (spider_name, date, url.replace('http://', ''))
        print(order)
        pi = Popen(order, shell=True, stdout=PIPE)
        result = int(pi.stdout.read())
        print(result)
        number.append(result)
    return number
