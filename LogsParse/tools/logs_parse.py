# -*-coding: utf-8 -*-
import os
import sys
sys.path.append('/www/wwwroot/LogsParse_for_web/')
from LogsParse.DBtools.dbhelper import DBHelper
import _thread


def insert(data, db):
    sql = 'INSERT spider.spider_num_of_url' \
          '(spider_ip, spider_date, spider_time, spider_name, target_url, group_name)' \
          ' VALUES (%s,%s,%s,%s,%s,%s)'
    param = (data[0], data[1], data[2], data[3], data[4], data[5])
    db.insert(sql, param)


def read_logs(file_name):
    try:
        db = DBHelper()
        file_baidu = open('/www/wwwroot/xbw/temp/robotlog/Baiduspider/%s' % file_name, 'r+')
        for line in file_baidu:
            data = line.split('\t')
            temp = [data[0].split(' ')[0], data[0].split(' ')[1], data[1], data[2], data[3].split('/', 3)[2],
                    data[4].strip('\n')]
            print('%s ### %s'% (file_name, temp))
            insert(temp, db)
        print('插入完毕')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        print('start')
        file_name = os.listdir('/www/wwwroot/xbw/temp/robotlog/Baiduspider/')
        for name in file_name:
            _thread.start_new_thread(read_logs, (name,))
        file_name = os.listdir('/www/wwwroot/xbw/temp/robotlog/360Spider/')
        for name in file_name:
            _thread.start_new_thread(read_logs, (name,))
        file_name = os.listdir('/www/wwwroot/xbw/temp/robotlog/Yisouspider/')
        for name in file_name:
            _thread.start_new_thread(read_logs, (name,))
        file_name = os.listdir('/www/wwwroot/xbw/temp/robotlog/sogou/')
        for name in file_name:
            _thread.start_new_thread(read_logs, (name,))
    except Exception as e:
        print(e)
        print("Error: 无法启动线程")
    while 1:
        pass