from app import create_app, db
from app.models import  Task
# from app.models import Task

app = create_app()


# @app.route('/')
# def home():
#     return "Hello wolrd"

with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app.run(debug=True)