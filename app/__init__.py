from flask import Flask

app = Flask(__name__)

app.config['PREFERRED_URL_SCHEME'] = 'https'

from app import routes
