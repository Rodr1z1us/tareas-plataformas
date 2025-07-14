from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

usuarios_bp = Blueprint('usuarios', __name__)

# Base de datos simulada
USUARIOS_DB = {
    "123": {"nombre": "Juan Pérez", "email": "juan@example.com"},
    "456": {"nombre": "María García", "email": "maria@example.com"},
    "789": {"nombre": "Carlos López", "email": "carlos@example.com"}
}

@usuarios_bp.route('/saludo')
def saludo_usuario():
    if 'id' in request.args:
        # Si viene con parámetro id, mostrar lista completa
        return jsonify({
            "mensaje": "Lista de usuarios completa",
            "usuarios": USUARIOS_DB,
            "total_usuarios": len(USUARIOS_DB),
            "fecha_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    else:
        # Si no viene con parámetro, mostrar la DB completa
        return jsonify({
            "mensaje": "Base de datos de usuarios",
            "data": USUARIOS_DB,
            "total_registros": len(USUARIOS_DB),
            "status": "success",
            "timestamp": datetime.now().isoformat()
        })