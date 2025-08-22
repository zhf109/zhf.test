from flask import Blueprint,session,redirect,render_template,request
from utils import db
from flask import url_for
od=Blueprint("order",__name__)

@od.route('/order/list')
def order_list():
    user_info = session.get("user_info")
    role = user_info['role']#1-客户   2-管理员
    if role==2:
        #data_list=db.fetch_all("select * from `order`",[])
        data_list=db.fetch_all(
            "select * from `order` left join user_info on `order`.user_id=user_info.id",[])
        #增加联表查询  下面同样（优化）
    else:
        data_list = db.fetch_all(
            "select * from `order` left join user_info on `order`.user_id=user_info.id where user_id=%s",
            [user_info['id'],])
    state_dict={
        1:{"text":"待执行",'cls':"primary"},
        2:{"text":"正在执行",'cls':"info"},
        3:{"text":"完成",'cls':"success"},
        4:{"text":"失败",'cls':"danger"},

    }#将数据库中的状态以中文输出   并根据不同状态赋予不同颜色（需要配合html）css素材的徽章
     #<span class="badge text-bg-secondary">Secondary</span>
     #<span class="badge text-bg-颜色控制">内容名字y</span>
    return render_template(
        "order_list.html",data_list=data_list,state_dict=state_dict,real_name=user_info['real_name'])




@od.route('/order/create' , methods=["GET","POST"])
def order_create():
    if request.method == "GET":
        return render_template('order_create.html')
    url = request.form.get('url')
    count = request.form.get('count')

    # 写入数据库
    user_info = session.get("user_info")
    params = [url,count,user_info['id']]
    db.insert("insert into `order` (url,count,user_id,state)values(%s,%s,%s,1)",params)
    return redirect('/order/list')




# 删除订单
@od.route('/order/delete' , methods=["GET","POST"])
def order_delete():
    if request.method == "GET":
        return render_template('order_delete.html')
    id = request.form.get('id')
    db.delete("DELETE FROM `order` WHERE id = %s ", (id))
    return redirect('/order/list')



# 修改订单
@od.route('/order/update' , methods=["GET","POST"])
def order_update():
    if request.method == "GET":
        return render_template('order_update.html')
    id = request.form.get('id')
    # url = request.form.get('url')
    # count = request.form.get('count')
    update_data = {
        'url': request.form.get('url'),
        'count': request.form.get('count'),
        'status': 1  # 根据业务需求设置状态
    }
    db.update(
        "UPDATE `order` SET url = %s, count = %s WHERE id = %s",
        (update_data['url'], update_data['count'], id)
    )
    return redirect('/order/list')



#查询订单
@od.route('/order/select' , methods=["GET","POST"])
def order_select():
    if request.method == "GET":
        return render_template('order_select.html')
    id = request.form.get('id')
    data_list = db.select("SELECT * FROM `order` WHERE id = %s", (id,))
    # print(data_list,123)  验证是否查询到数据
    state_dict={
        1:{"text":"待执行",'cls':"primary"},
        2:{"text":"正在执行",'cls':"info"},
        3:{"text":"完成",'cls':"success"},
        4:{"text":"失败",'cls':"danger"},
                }
    return render_template(
        "order_list.html", data_list=data_list, state_dict=state_dict)






