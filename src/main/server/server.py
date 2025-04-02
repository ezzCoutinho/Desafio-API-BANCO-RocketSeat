from flask import Flask
from flask_cors import CORS

from src.main.server.routes.pessoa_fisica_routes import pessoa_fisica_routes_bp
from src.main.server.routes.pessoa_juridica_routes import pessoa_juridica_routes_bp
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pessoa_fisica_routes_bp)
app.register_blueprint(pessoa_juridica_routes_bp)
