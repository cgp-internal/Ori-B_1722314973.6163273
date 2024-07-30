from flask import Flask
from routes.notes import notes_router
from app_config import DB_PATH

app = Flask(__name__)

app.register_blueprint(notes_router, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)