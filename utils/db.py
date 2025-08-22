import pymysql
from pymysql import cursors
from dbutils.pooled_db import PooledDB
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

def fetch_one(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    result =cursor.fetchone()
    cursor.close()
    return result


def fetch_all(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    result =cursor.fetchall()
    cursor.close()
    return result


def insert(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    conn.commit()
    cursor.close()
    conn.close()


def delete(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    conn.commit()
    cursor.close()
    conn.close()


def update(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    conn.commit()
    cursor.close()
    conn.close()


def select(sql,params):
    conn =POOL.connection()
    cursor=conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql,params)
    result = cursor.fetchall()  # 获取所有结果
    cursor.close()
    conn.close()
    return result
