# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def index():
#   return "Hello World"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example'
db = SQLAlchemy(app)