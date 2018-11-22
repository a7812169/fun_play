from . import order
from .services import *
from os import path
from flask import render_template,redirect,request,url_for
from flask import jsonify
from app import make_error,make_success
@order.route('/',methods=['GET','POST'])
def add_one():
    data=get_all_news()
    return jsonify(make_success(data=data))
