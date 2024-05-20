from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Removed import (not used)

app = Flask(__name__)

# Removed database configuration (not used)

app.config['PREFERRED_URL_SCHEME'] = 'https'

# db = SQLAlchemy(app)  # Removed (not used)

from app import routes
