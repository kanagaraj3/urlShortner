from flask import request, jsonify, render_template, redirect
import string
import random

from app import app

def generate_short_url():
  characters = string.ascii_letters + string.digits
  while True:
    short_url = ''.join(random.choice(characters) for _ in range(6))
    # No need to check for existing URLs in the database
    return short_url

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
  original_url = request.form.get('original_url')
  if not original_url:
    return jsonify({'error': 'No URL provided'}), 400
  short_url = generate_short_url()
  # Don't call save_url(), directly construct the shortened URL
  return jsonify({'short_url': f'https://url-shortner-git-main-kanagarajs-projects.vercel.app/{short_url}'})

@app.route('/<short_url>')
def redirect_to_url(short_url):
  # No need to query the database for original URL
  # Consider a mechanism to validate the short URL format here
  return redirect(f"https://{short_url}")  # Assuming the short URL format is valid
