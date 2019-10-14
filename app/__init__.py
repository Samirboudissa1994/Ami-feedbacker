from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from app.queries import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin


app = Flask(__name__)


app.config['SECRET_KEY'] = '0c6jFZgojaMg87Es'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['BASIC_AUTH_FORCE'] = True
app.config['BASIC_AUTH_USERNAME'] = 'project'
app.config['BASIC_AUTH_PASSWORD'] = 'one'
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Kirjaudu sisään ensiksi'

basic_auth = BasicAuth(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"


from app import routes

create_tables()
