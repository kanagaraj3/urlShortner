from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../urls.db'
app.config['PREFERRED_URL_SCHEME'] = 'https'
db = SQLAlchemy(app)

from app import routes
