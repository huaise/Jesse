import os
from app import new_app

app = new_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8080, debug = True)
