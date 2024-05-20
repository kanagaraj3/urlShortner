# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:Z4Qo2WtBFwDN@ep-nameless-water-a4whe7o1.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
app.config['PREFERRED_URL_SCHEME'] = 'https'
db = SQLAlchemy(app)

from app import routes
