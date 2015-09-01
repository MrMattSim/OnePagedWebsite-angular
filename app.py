from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text

app = Flask(__name__, static_url_path='')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    date = Column(Text, unique=False)
    description = Column(Text, unique=False)


db.create_all()
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Project, methods=['GET'])


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
