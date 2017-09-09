from flask import render_template, url_for
from . import main 
from ..models import Category

@main.route('/', methods = ['GET'])
def index():
	return render_template('main/index.html')

@main.route('/home', methods = ['GET'])	
def home():
	categorys = Category.query.order_by(Category.count)
	return render_template('main/home.html', categorys=categorys)