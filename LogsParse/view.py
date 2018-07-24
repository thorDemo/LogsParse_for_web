# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from LogsParse.libs.ssh_data import SSHClient
from subprocess import PIPE, Popen
import datetime
import os
from LogsParse.tools.search_group import insert_spider_group_url
import glob


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
        print(e)
        return HttpResponse(json.dumps({'message': 'exception %s' % url}))
    return HttpResponse(json.dumps({'message': 'this is group %s' % group_id}))


# 获取域名分组信息
def search_dir(request):
    group_id = request.GET.get('group_id')
    path = os.path.abspath('.')
    data = dict()
    # if group_id == '8':
    dir = os.listdir('%s/LogsParse/domain' % path)
    for file in dir:
        urls = []
        domain = open('%s/LogsParse/domain/%s/domain.txt' % (path, file), 'r+')
        for line in domain:
            urls.append(line.strip('\n'))
        data[file] = urls
    # else:
    #     pass
        # print(group_id)
        # client = SSHClient(str(group_id))
        # ssh = client.ssh_connect()
        # data = client.search_dir(ssh)
    return HttpResponse(json.dumps(data))


# 查询url的蜘蛛数量
def search_url(request):
    url = str(request.GET.get('spider_url')).split(' ')[2]
    group_id = request.GET.get('group_ip')
    print(group_id)
    # if group_id == '8' or group_id is None:
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
    result['title'] = '蜘蛛池 域名：%s' % url
    result['category'] = category
    result['Baiduspider'] = Baidu
    result['Yisouspider'] = Yisouspider
    result['360Spider'] = Spider360
    result['sogou'] = sogou
    return HttpResponse(json.dumps(result))
    # else:
    #     pass
        # client = SSHClient(str(group_id))
        # ssh = client.ssh_connect()
        # result = client.spider_number(ssh, url=url)
        # result['title'] = '%s组蜘蛛池 域名：%s' % (group_id, url)
        # ssh.close()
        # print(result)
        # return HttpResponse(json.dumps(result))


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
