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