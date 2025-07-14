from flask import Flask
from flask_cors import CORS
from .controllers.usuarios import usuarios_bp

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config['JSON_SORT_KEYS'] = False
    
    # CORS
    CORS(app, resources={
        r"/usuarios/*": {"origins": "*"}
    })
    
    # Blueprints
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios/api/v1')
    
    return app