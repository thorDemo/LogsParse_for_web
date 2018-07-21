# -*- coding: utf-8 -*-
import paramiko
from django.conf import settings
from paramiko.ssh_exception import SSHException
import datetime
import time


class SSHClient:
    # 配置链接
    def __init__(self, host='23.110.211.170', port=22, user='root', pwd=''):
        self.SPIDER_HOST = host
        self.SPIDER_PORT = port
        self.SPIDER_USER = user
        self.SPIDER_PWD = pwd
        self.XBW_PATH = '/www/wwwroot/xbw/temp/robotlog/'
        self.NOW = datetime.datetime.now().strftime('%Y%m%d')
        self.num = 0

    # 创建链接
    def ssh_connect(self):
        _ssh_fd = paramiko.SSHClient()
        try:
            _ssh_fd.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            _ssh_fd.connect(self.SPIDER_HOST, username=self.SPIDER_USER, password=self.SPIDER_PWD, allow_agent=False, look_for_keys=False)
            print('connect success!')
            return _ssh_fd
        except SSHException as e:
            print('reload connect')
            _ssh_fd.close()
            self.ssh_connect()
            self.num += 1

    # 执行CMD 命令
    def ssh_exec_cmd(self, _ssh_fd, cmd):
        print("exec command %s \n%s" % (self.SPIDER_HOST, cmd))
        return _ssh_fd.exec_command(cmd, get_pty=True)

    # 查询蜘蛛数量
    def spider_number(self,ssh, url):
        spider_num = []
        cmd = ''
        spider_name = ['Baiduspider','Yisouspider','360Spider','sogou']
        category, logs_num = self.search_logs(ssh)
        for line in spider_name:
            for day in category:
                cmd += 'cat /www/wwwroot/xbw/temp/robotlog/%s/%s |grep %s|wc -l;' % (line, day, url)
        stdin, stdout, stderr = self.ssh_exec_cmd(ssh,cmd)
        err_list = stderr.readlines()
        if len(err_list) > 0:
            print('ERROR:' + err_list[0])
            return None

        for item in stdout:
            try:
                spider_num.append(int(item.strip('\r\n')))
            except ValueError:
                spider_num.append(0)
        return spider_num, logs_num

    def search_logs(self, ssh):
        category = []
        logs_num = []
        cmd = 'cd /www/wwwroot/xbw/temp/robotlog/Baiduspider/;ls'
        stdin, stdout, stderr = self.ssh_exec_cmd(ssh, cmd=cmd)
        for item in stdout:
            logs_name = str(item).replace('\t', '  ').strip('\r\n').split('  ')
            for name in logs_name:
                logs_num.append(name[4:8])
                category.append(name)
        return sorted(category, key=lambda x: x[0:8]), sorted(logs_num, key=lambda x:x[0:4])


def main():
    Client= SSHClient()
    ssh = Client.ssh_connect()
    spider_num, logs_num = Client.spider_number(ssh, url='aidshe.com')
    ssh.close()
    print(logs_num)
    print(spider_num)



