from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///urls.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes
