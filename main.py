from app import app
from app.config import Config

if __name__ == '__main__':
    app.config.from_object(Config)
    app.run(debug=True)
