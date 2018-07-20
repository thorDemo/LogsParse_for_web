# -*- coding=utf-8 -*-
import os
import sys
sys.path.append('/www/wwwroot/LogsParse_for_web/')
import paramiko
from LogsParse.libs.data import SSHClient
from LogsParse.DBtools.dbhelper import DBHelper


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


def insert_spider_group_url(group_id, url):
    data_base = DBHelper()
    if group_id == '9':
        path = '/www/wwwroot/LogsParse_for_web'
        dirs = os.listdir('%s/LogsParse/domain' % path)
        for file in dirs:
            domain = open('%s/LogsParse/domain/%s/domain.txt' % (path, file), 'r+')
            for line in domain:
                sql = 'INSERT spider_group_url (spider_url, spider_group, spider_tips)' \
                      'VALUES (%s,%s,%s)' % (line, group_id, file)
                print(sql)
                data_base.insert(sql=sql)
    else:
        print('this is group %s' % group_id)
