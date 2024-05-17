from flask import Flask, request, jsonify, render_template, redirect
import string
import random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['PREFERRED_URL_SCHEME'] = 'https'
db = SQLAlchemy(app)
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(10), unique=True)
    original_url = db.Column(db.String(255), nullable=False)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if not URL.query.filter_by(short_url=short_url).first():
            return short_url

def save_url(short_url, original_url):
    try:
        db.session.add(URL(short_url=short_url, original_url=original_url))
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False

def get_original_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    return url.original_url if url else None

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['original_url']
    short_url = generate_short_url()
    if save_url(short_url, original_url):
        return jsonify({'short_url': request.host_url + short_url})
    else:
        return jsonify({'error': 'Failed to save URL'}), 500

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
