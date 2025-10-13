# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initialize extensions out of create_app
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

# login_manager.login_view = 'auth.login'
# login_manager.login_message_category = 'info'

# Factory function create app
def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('config.py')

    # Init extensions with app
    db.init_app(app)

    # Register blueprint
    from .auth import auth_bp
    from .notes import notes_bp
    from .share import share_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(share_bp, url_prefix='/share')

    return app
