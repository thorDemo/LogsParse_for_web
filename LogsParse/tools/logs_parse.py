# -*-coding: utf-8 -*-
import os
import sys
sys.path.append('/www/wwwroot/LogsParse_for_web/')
import subprocess


def insert(data, db):
    sql = 'INSERT spider_num_of_url(spider_date, spider_name, target_url, spider_num)' \
          'VALUES(%s,%s,%s,%s)'
    param = (data[0], data[1], data[2], data[3])
    db.insert(sql, param)


def read_logs(url, date):
    path = os.path.abspath('.')
    try:
        spider = ['Baiduspider', '360Spider', 'sogou', 'Yisouspider']
        for line in spider:
            order = 'cat /www/wwwroot/xbw/temp/robotlogs/%s/%s |grep %s|wc -l' % (line, date, url)
            pi = subprocess.Popen(order, shell=True,stdout=subprocess.Popen)
            result = pi.stdout.read().strip('\n')
            cookie = open('%s/LogsParse/cookie/%s' % (path, url), 'a+')
            cookie.write('%s %s %s' % (date.strip('.log'), url, result))
            print('%s %s %s' % (date, url, result))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        urls = []
        path = os.path.abspath('.')
        dates = os.listdir('/www/wwwroot/xbw/temp/robotlog/Baiduspider/')
        group = os.listdir('%s/LogsParse/domain' % path)
        for file in group:
            domain = open('%s/LogsParse/domain/%s/domain.txt' % (path, file), 'r+')
            for line in domain:
                urls.append(line.strip('\n'))
        for url in urls:
            for date in dates:
                read_logs(url, date)
    except Exception as e:
        print(e)
