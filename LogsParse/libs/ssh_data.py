# -*- coding: utf-8 -*-
import paramiko
from django.conf import settings
from paramiko.ssh_exception import SSHException
import datetime
import time

ssh_data = {
    '1': {'host': '142.234.162.99', 'port': 22, 'pwd': 'free@0516'},
    '2': {'host': '209.58.128.89', 'port': 22, 'pwd': 'E6zJ01V7Ykig'},
    '3': {'host': '198.56.192.250', 'port': 22, 'pwd': 'snow1029'},
    '4': {'host': '104.243.140.166', 'port': 22, 'pwd': 'Ptyw1q2w3e$R'},
    '5': {'host': '142.234.255.29', 'port': 22, 'pwd': 'AzVWuhQa1773'},
    '6': {'host': '45.34.107.130', 'port': 22, 'pwd': 'free0714'},
    '7': {'host': '45.42.95.170', 'port': 22, 'pwd': 'Ptyw1q2w3e$R'},
    '8': {'host': '142.234.162.79', 'port': 22, 'pwd': 'Vfc4RV1C01oy'},
    '9': {'host': '23.110.211.170', 'port': 223, 'pwd': 'Hxt414722027'},
    '10': {'host': '23.80.91.154', 'port': 22, 'pwd': 'free0514'},
}


class SSHClient:
    # 配置链接
    def __init__(self, group_id):
        self.SPIDER_HOST = ssh_data[group_id]['host']
        self.SPIDER_PORT = ssh_data[group_id]['port']
        self.SPIDER_USER = 'root'
        self.SPIDER_PWD = ssh_data[group_id]['pwd']
        self.XBW_PATH = '/www/wwwroot/xbw/temp/robotlog/'
        self.NOW = datetime.datetime.now().strftime('%Y%m%d')
        self.num = 0

    # 创建链接
    def ssh_connect(self):
        # try:
        _ssh_fd = paramiko.SSHClient()
        try:
            _ssh_fd.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            _ssh_fd.connect(self.SPIDER_HOST, username=self.SPIDER_USER, password=self.SPIDER_PWD, port=self.SPIDER_PORT, allow_agent=False, look_for_keys=False)
            print('connect success!')
            return _ssh_fd
        except SSHException as e:
            print('reload connect')
            _ssh_fd.close()
            self.ssh_connect()
            self.num += 1
        # except:
        #     self.num += 1
        #     if self.num > 4:
        #         return None
        #     print('except reload')
        #     self.ssh_connect()

    # 执行CMD 命令
    def ssh_exec_cmd(self, _ssh_fd, cmd):
        print("exec command %s \n%s" % (self.SPIDER_HOST, cmd))
        return _ssh_fd.exec_command(cmd, get_pty=True)

    # 查询蜘蛛数量
    def spider_number(self, ssh, url):
        data = dict()
        spider_name = ['Baiduspider','Yisouspider','360Spider','sogou']
        category, logs_num = self.search_logs(ssh)
        for line in spider_name:
            spider_num = []
            cmd = ''
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
            data[line] = spider_num
        data['category'] = logs_num
        return data

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

    def search_dir(self, ssh):
        dirs = []
        group_url = dict()
        cmd = 'cd /www/wwwroot/xbw/temp/data/domain/;ls -l|grep "^d"'
        stdin, stdout, stderr = self.ssh_exec_cmd(ssh, cmd=cmd)
        for item in stdout:
            domain_dir = str(item).split(' ')[-1].strip('\r\n')
            dirs.append(domain_dir)
            print(domain_dir)
        print(dirs)
        for domain in dirs:
            temp = []
            cmd = 'cat /www/wwwroot/xbw/temp/data/domain/%s/domain.txt' % domain
            stdin, stdout, stderr = self.ssh_exec_cmd(ssh, cmd=cmd)
            for item in stdout:
                temp.append(str(item).split('\r\r\n')[0])
            group_url[domain] = temp
        return group_url


def main():
    client = SSHClient('2')
    ssh = client.ssh_connect()
    # group_url = client.search_dir(ssh)
    # print(group_url)
    result = client.spider_number(ssh, 'btbse.com')
    print(result)
    ssh.close()


if __name__ == '__main__':
    main()

