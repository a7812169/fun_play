from flask import Flask
from flask.ext.bootstrap import Bootstrap

from .msyql import DB
def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    bootstrap = Bootstrap(app)

    from .control import control
    from .top import top
    # from .order import order
    # app.register_blueprint(new_spider,url_prefix='/news')
    app.register_blueprint(control,url_prefix='/index')
    app.register_blueprint(top,url_prefix='/top')
    # app.register_blueprint(order,url_prefix='/funs')
    # app.register_blueprint(qa,url_prefix='/qa')
    return app
def get_connection():
    db = DB('120.79.227.7', 3306, 'root', '7812169', 'fun_play')
    return db.getConnection()
def make_error(code=0, msg='请求失败', data=None):
    return {
        'error': {
            'code': code,
            'msg': msg,
            'data': data
        }
    }
def make_success(code=1, msg='请求成功', data=None):
    return {
        'code': code,
        'msg': msg,
        'data': data
    }