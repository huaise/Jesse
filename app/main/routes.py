from flask import render_template, url_for, request, redirect
from . import main 
from ..models import Category,Post

PAGE_COUNT = 8

@main.route('/', methods = ['GET'])
def index():
	return render_template('main/index.html')

@main.route('/home', methods = ['GET'])	
def home():
	page = request.args.get('page', 1, type=int)
	categorys = Category.query.order_by(Category.count.desc())
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page = PAGE_COUNT, error_out = False)
	posts = pagination.items
	return render_template('main/home.html', categorys=categorys, posts=posts, pagination=pagination)

@main.route('/category/<tag>', methods = ['GET'])
def category(tag):
	page = request.args.get('page', 1, type=int)
	tag = Category.query.filter_by(tag=tag).first_or_404()
	pagination = Post.query.filter_by(category_id = tag.id).order_by(Post.timestamp.desc()).paginate(page, per_page = PAGE_COUNT, error_out = False)
	posts = pagination.items
	categorys = Category.query.order_by(Category.count.desc())
	return render_template('main/home.html', categorys=categorys, posts=posts, pagination=pagination, tag=tag)

@main.route('/post/<int:id>',methods=['GET'])
def post(id):
	post = Post.query.get_or_404(id)
	categorys = Category.query.order_by(Category.count)
	return render_template("main/post.html", post=post, categorys=categorys, category_hidden=True)
@main.route('/about')
def about():
	return render_template("main/about.html", category_hidden=True)

@main.app_errorhandler(404)
def page_not_found(error):
	return render_template("public/404.html", category_hidden=True),404