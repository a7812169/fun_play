from flask import Blueprint
top=Blueprint('top',__name__,template_folder='templates')
from . import views