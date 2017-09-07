from flask import Flask,render_template

def new_app(config_name):
	app = Flask(__name__)

	# load home page
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	# load admin page
	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	# run obj
	return app 