from . import top
from .services import *
from os import path
from flask import render_template,redirect,request,url_for
from flask import jsonify
from app import make_error,make_success
@top.route('/',methods=['GET','POST'])
def tops():
    data=get_all_news()
    return jsonify(make_success(data=data))
@top.route('/top_10',methods=['GET','POST'])
def top_10():
    data=get_top10_funplay()
    return jsonify(make_success(data=data))
@top.route('/get_new_by_type/<int:type>',methods=['GET'])
def get_new_by_typ(type):
    data=get_new_by_type(type)
    return jsonify(make_success(data=data))
@top.route('/get_order/<name>',methods=['GET'])
def order(name):
    data=get_order(name)
    return jsonify(make_success(data=data))
@top.route('/get_recommend',methods=['POST'])
def get_recommand():
    form=dict(request.get_json())
    count=0
    table={"儿童":10,"水上":40,"刺激":80,"娱乐演出":30,"旋转木马":10,"花车巡游":20,"烟火秀":20,"浪漫":10,"拍照":10}
    for i in form.keys():
        count+=table[i]
    get_done(count)
    data="更新完成"
    return jsonify(make_success(data=data))
