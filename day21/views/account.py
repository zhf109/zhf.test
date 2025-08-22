from flask import Blueprint,render_template,request,redirect,session
import pymysql
from utils import db




ac=Blueprint("account",__name__)

@ac.route('/login',methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")

    role = request.form.get("role")
    mobile = request.form.get("mobile")
    pwd = request.form.get("pwd")


                         #连接mysql并验证信息是否正确
    # conn=pymysql.connect(
    #     host='127.0.0.1',
    #     port=3306,
    #     user='root',
    #     password='123456',
    #     charset='utf8',
    #     db='day21'
    # )
    # cursor=conn.cursor()
    # cursor.execute("select * from user_info where role=%s and mobile=%s and password=%s",[role,mobile,pwd])
    # user_dict=cursor.fetchone()
    # cursor.close()
    # conn.close()
    user_dict=db.fetch_one("select * from user_info where role=%s and mobile=%s and password=%s",[role,mobile,pwd])

    if user_dict:
        #登录成功+跳转
        #将用户信息封装进cookie
        session["user_info"]={"role":user_dict['role'],'real_name': user_dict['name'],'id': user_dict['id']}
        return redirect('/order/list')
    return render_template("login.html",error="用户名或密码错误")




@ac.route('/user')
def user():
    return "用户列表"
