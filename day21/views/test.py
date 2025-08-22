import pymysql
from pymysql import cursors
from dbutils.pooled_db import PooledDB

from flask import Blueprint,session,redirect,render_template,request
from utils import db
from flask import url_for
od=Blueprint("order",__name__)

POOL=PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    setsession=[],
    ping=0,

    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    db='day21'
)


def select(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    result = cursor.fetchall()  # 获取所有结果
    cursor.close()
    conn.close()
    return result




# def select(sql, params):
#     conn = POOL.connection()
#     cursor = conn.cursor(cursor=cursors.DictCursor)
#     try:
#         cursor.execute(sql, params)
#         result = cursor.fetchall()  # 获取所有结果
#         return result
#     except Exception as e:
#         print("SQL Error:", str(e))
#         return None
#     finally:
#         cursor.close()
#         conn.close()






id = 1
print(id,258)
result=select("SELECT * FROM `order` WHERE id = %s", (id,))

print(result,123)


