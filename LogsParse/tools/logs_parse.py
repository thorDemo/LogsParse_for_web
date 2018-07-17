# -*-coding: utf-8 -*-
import os
from LogsParse.DBtools.dbhelper import DBHelper
import _thread


def insert(data, db):
    sql = 'INSERT spider.spider_num_of_url' \
          '(spider_ip, spider_date, spider_time, spider_name, target_url, group_name)' \
          ' VALUES (%s,%s,%s,%s,%s,%s)'
    param = (data[0], data[1], data[2], data[3], data[4], data[5])
    db.insert(sql, param)


def read_logs(spider_name):
    try:
        db = DBHelper()
        path = '/www/wwwroot/xbw/temp/robotlogs/'
        file_name = os.listdir(path)
        for name in file_name:
            file_baidu = open('%s%s/%s' % (path, spider_name, name), 'r+')
            for line in file_baidu:
                data = line.split('\t')
                temp = [data[0].split(' ')[0], data[0].split(' ')[1], data[1], data[2], data[3].split('/', 3)[2],
                        data[4].strip('\n')]
                insert(temp, db)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        print('start')
        _thread.start_new_thread(read_logs, ('Baiduspider',))
        _thread.start_new_thread(read_logs, ('360Spider',))
        _thread.start_new_thread(read_logs, ('Yisouspider',))
        _thread.start_new_thread(read_logs, ('sogou',))

    except Exception as e:
        print(e)
        print("Error: 无法启动线程")
    while 1:
        pass