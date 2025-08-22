from flask import Flask,request,session,redirect

def auth():#拦截器
    print(request.path,type(request.path))#

    if request.path.startswith("/static"):#防止拦截静像文件
        return

    if request.path=='/login':    #如果
        return

    user_info=session.get("user_info")
    if user_info:
        return


    return redirect('/login')

def get_real_name():  #用函数把信息传给html
    user_info =session.get("user_info")
    return user_info['real_name']

def create_app():
    app = Flask(__name__)

    app.secret_key='zhanghangfei'  #设置cookie密钥

    from .views import account
    from .views import order
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)

    app.before_request(auth)  #拦截器
    app.template_global()(get_real_name)
    return app