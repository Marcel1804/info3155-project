from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"  # you should make this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://qbvcdjtaqcmfbv:2dc56da5ef0e4125f5ed56e8ab26d8a30ddf64527fa56caddb28cc0e134f1e8e@ec2-23-23-177-166.compute-1.amazonaws.com:5432/dbauqnerlit3bt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER='./app/static/uploads'

app.config.from_object(__name__)

# using a config value
filefolder=app.config['UPLOAD_FOLDER']
from app import views
