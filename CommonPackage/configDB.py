#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 20:35
# @Author  : william
# @Site    : 
# @File    : configDB.py
# @Software: PyCharm

import  pymysql

db = pymysql.connect(host ="localhost",user='root',password='xwj123456',port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version',data)
cursor.execute("Create DATABASE spiders DEFAULT CHARACTER  SET UTF8")
db.close()