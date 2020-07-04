from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '93f900f5292f0c3de38c0694e92bb79a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from server import routes