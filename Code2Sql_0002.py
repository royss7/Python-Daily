#!/usr/local/bin/python2.7

'''
 ********************************************
 * Name        : Code2Sql-0002.py
 * Discription : Save the codes to mysql with relationship database
 * Date        : 2015-06-24
 * Author      : liuyy"
 * E-mail      : liuyy2006@163.com"
 ********************************************
'''

import sys
if sys.version_info.major > 2:
    print("Only suport up to python2.7")
    sys.exit()

# Only support python2
import MySQLdb
import Code_0001



#                      host         user    password    database
db = MySQLdb.connect('localhost', 'guest', 'guest123', 'test')

# operation cursor
c = db.cursor()

# execute the database
# show version of database
c.execute("SELECT VERSION()")

# get data
d = c.fetchone()


# Create a new talbe for discount coupon
c.execute("DROP TABLE IF EXISTS DiscountCoupon")
sql = """CREATE TABLE DiscountCoupon(
        code char(9) not null primary key,
        isUsed tinyint null
        );"""
c.execute(sql)

# code generation
s = [chr(i) for i in range(0 + ord('0'), 10 + ord('0'))]
for i in range(ord('A'), ord('Z') + 1):
    s.append(chr(i))
codes = Code_0001.safe_gen(s)

for i in codes:
    insertMsg = """INSERT INTO DiscountCoupon VALUES(\"{0}\", 0)""".format(i)
    try:
        c.execute(insertMsg)
        # apply the change
        db.commit()
    except:
        db.rollback()

db.close()
