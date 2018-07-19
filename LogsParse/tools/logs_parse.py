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


def read_logs(_url, _date):
    _path = os.path.abspath('.')
    try:
        spider = ['Baiduspider', '360Spider', 'sogou', 'Yisouspider']
        for y in range(0, 3):
            order = 'cat /www/wwwroot/xbw/temp/robotlog/%s/%s |grep %s|wc -l' % (spider[y], _date, _url)
            print(order)
            pi = Popen(order, shell=True, stdout=PIPE)
            result = pi.stdout.read()
            cookie = open('/www/wwwroot/LogsParse_for_web/LogsParse/cookie/%s' % _url, 'a+')
            cookie.write('%s %s %s' % (date.strip('.log'), _url, result.strip('\n')))
            print('%s %s %s' % (_date, _url, result))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        print('take in process!')
        urls = []
        path = '/www/wwwroot/LogsParse_for_web/LogsParse/'
        group = os.listdir('/www/wwwroot/LogsParse_for_web/LogsParse/domain/')
        for file in group:
            domain = open('%sdomain/%s/domain.txt' % (path, file), 'r')
            for line in domain:
                urls.append(line.strip('\n'))
        print(urls)
        for x in (0, len(urls)):
            print('agent !')
            dates = os.listdir('/www/wwwroot/xbw/temp/robotlog/Baiduspider/')
            for date in dates:
                print('%s %s' % (urls[x], date))
                read_logs(urls[x], date)
    except Exception as e:
        print(e)
