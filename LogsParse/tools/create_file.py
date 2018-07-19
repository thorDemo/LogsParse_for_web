# -*-coding=utf-8-*-
import os

files = os.listdir('../domain/')
for line in files:
    file = open('../domain/%s/domain.txt' % line, 'r+')
    for url in file:
        cookie = open('../cookie/%s' % url.strip('\n'), 'w+')