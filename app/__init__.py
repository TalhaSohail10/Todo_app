# from flask import Flask
# # form flask_sqlalchemy import SQLAlchemy
# # from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__,template_folder='templates', static_folder='static')
#     app.config['SECRET_KEY'] = 'secretkey1234'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app) 
    
#     from app.routes.auth import auth_bp
#     from app.routes.task import task_bp 
#     app.register_blueprint(auth_bp)
#     app.register_blueprint(task_bp)

#     with app.app_context():
#        db.create_all()
    
#     return app




# # Sector:5A-3, 192 ,quid e azam park , madina masjid , islamia college


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'secretkey1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Proper initialization
    db.init_app(app)

    # Import blueprints
    from app.routes.auth import auth_bp
    from app.routes.task import task_bp 
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    # Create tables inside app context
  

    return app
   