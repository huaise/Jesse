from flask import render_template, url_for, request
from . import main 
from ..models import Category,Post

PAGE_COUNT = 8

@main.route('/', methods = ['GET'])
def index():
	return render_template('main/index.html')

@main.route('/home', methods = ['GET'])	
def home():
	
	page = request.args.get('page', 1, type=int)
	categorys = Category.query.order_by(Category.count)
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page = PAGE_COUNT, error_out = False)
	posts = pagination.items
	return render_template('main/home.html', categorys=categorys, posts=posts, pagination=pagination)
