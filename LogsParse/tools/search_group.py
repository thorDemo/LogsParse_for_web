# -*- coding=utf-8 -*-
import os
import sys
sys.path.append('/www/wwwroot/LogsParse_for_web/')
import paramiko
from LogsParse.libs.ssh_data import SSHClient
from LogsParse.DBtools.dbhelper import DBHelper


def insert_spider_group_url(group_id, url):
    data_base = DBHelper()
    if group_id == '9':
        print('id = %s  url = %s ' % (group_id, url))
        path = '/www/wwwroot/LogsParse_for_web'
        dirs = os.listdir('%s/LogsParse/domain' % path)
        for file in dirs:
            domain = open('%s/LogsParse/domain/%s/domain.txt' % (path, file), 'r+')
            for line in domain:
                sql = 'INSERT spider_group_url (spider_url, spider_group, spider_tips)' \
                      'VALUES ("%s","%s","%s")' % (line, group_id, file)
                print(sql)
                data_base.insert(sql=sql)
    else:
        print('this is group %s' % group_id)
