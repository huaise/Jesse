from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config
from flask.ext.markdown import Markdown

db = SQLAlchemy()
markdown = Markdown

def new_app():
	app = Flask(__name__)

	app.config.from_object(Config)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	db.init_app(app)
	markdown(app)
	
	# load home page
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	# load admin page
	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	from .models import Post,Category
	
	# run obj
	return app 