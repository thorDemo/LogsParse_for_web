# -*-coding: utf-8 -*-
import os
import sys
sys.path.append('/www/wwwroot/LogsParse_for_web/')
from subprocess import Popen, PIPE


def insert(data, db):
    sql = 'INSERT spider_num_of_url(spider_date, spider_name, target_url, spider_num)' \
          'VALUES(%s,%s,%s,%s)'
    param = (data[0], data[1], data[2], data[3])
    db.insert(sql, param)


def read_logs(url, date):
    path = os.path.abspath('.')
    try:
        spider = ['Baiduspider', '360Spider', 'sogou', 'Yisouspider']
        for x in range(0, 3):
            order = 'cat /www/wwwroot/xbw/temp/robotlog/%s/%s |grep %s|wc -l' % (spider[x], date, url)
            print(order)
            pi = Popen(order, shell=True, stdout=PIPE)
            result = pi.stdout.read()
            cookie = open('%s/LogsParse/cookie/%s' % (path, url), 'a+')
            cookie.write('%s %s %s' % (date.strip('.log'), url, result.strip('\n')))
            print('%s %s %s' % (date, url, result))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        print('take in process!')
        urls = []
        path = '/www/wwwroot/LogsParse_for_web/LogsParse/'
        dates = os.listdir('/www/wwwroot/xbw/temp/robotlog/Baiduspider/')
        print(dates)
        group = os.listdir('/www/wwwroot/LogsParse_for_web/LogsParse/domain/')
        print(group)
        for file in group:
            domain = open('%sdomain/%s/domain.txt' % (path, file), 'a+')
            for line in domain:
                urls.append(line.strip('\n'))
        for url in urls:
            for date in dates:
                read_logs(url, date)
    except Exception as e:
        print(e)
