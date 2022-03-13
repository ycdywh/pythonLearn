#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import mysql.connector

#连接数据库
conn = mysql.connector.connect(user='root',
                               password='root1234',
                               database='test')

cursor = conn.cursor()
#创建user表
cursor.execute(
    'create table user (id varchar(20) primary key, name varchar(20))')
#插入一行记录
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount=', cursor.rowcount)
#提交事务
conn.commit()
cursor.close()

#运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1', ))
values = cursor.fetchall()
print(values)
#关闭cursor和connection
cursor.close()
conn.close()