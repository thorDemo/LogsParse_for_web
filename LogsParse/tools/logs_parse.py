# -*-coding: utf-8 -*-
import os
import pymysql
import sys
from LogsParse.DBtools.dbhelper import DBHelper


class Spider:
    def __init__(self, date, time, ip, spider, url, group):
        self.date = date
        self.time = time
        self.ip = ip
        self.spider = spider
        self.url = url
        self.group = group

    def __del__(self):
        class_name = self.__class__.__name__


def insert(spider, db):
    sql = 'INSERT spider_count(group_name, spider_name, time_of_day,spider_num, spider_ip) VALUES (%S,%S,%S,%S,%S)'
    param = ()
    db.insert(sql, param)


def read_logs():
    db = DBHelper()
    path = '/www/wwwroot/xbw/temp/robotlogs/Baiduspider'
    file_name = os.listdir(path)
    for name in file_name:
        file_baidu = open('%s/%s' % (path,name), 'r+')
        for line in file_baidu:
            data = line.split(' ')
            spider = Spider(data[0], data[1], data[2], data[3], data[4], data[5])
            insert(spider, db)
            del spider

