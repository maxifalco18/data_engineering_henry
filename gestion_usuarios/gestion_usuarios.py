import json
from decouple import config
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []
        self.default_file = config("DEFAULT_FILE", default=os.getenv("DEFAULT_FILE", "usuarios.json"))

    def hash_contrasena(self, contrasena):
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

    def registrar_usuario(self, nombre, email, contrasena):
        if not nombre or not email or not contrasena:
            raise ValueError("Todos los campos son obligatorios.")
        if "@" not in email or "." not in email:
            raise ValueError("El email no tiene un formato válido.")
        if any(u["email"] == email for u in self.usuarios):
            raise ValueError("El email ya está registrado.")
        usuario = {
            "nombre": nombre,
            "email": email,
            "contrasena": self.hash_contrasena(contrasena)
        }
        self.usuarios.append(usuario)
        return usuario

    def listar_usuarios(self):
        return [
            {"nombre": u["nombre"], "email": u["email"]}
            for u in self.usuarios
        ]

    def buscar_usuario(self, nombre):
        resultados = [u for u in self.usuarios if nombre.lower() in u["nombre"].lower()]
        return resultados

    def eliminar_usuario(self, nombre):
        resultados = [u for u in self.usuarios if nombre.lower() in u["nombre"].lower()]
        if not resultados:
            raise ValueError(f"No se encontraron usuarios con el nombre que contiene: {nombre}")
        usuario_eliminado = resultados[0]
        self.usuarios = [u for u in self.usuarios if u != usuario_eliminado]
        return usuario_eliminado

    def guardar_usuarios(self, archivo=None):
        archivo = archivo or self.default_file
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(self.usuarios, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            raise IOError(f"Error al guardar usuarios en {archivo}: {e}")

    def cargar_usuarios(self, archivo=None):
        archivo = archivo or self.default_file
        if not os.path.exists(archivo):
            self.usuarios = []
            return False
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            if self.validar_estructura(data):
                self.usuarios = data
                return True
            else:
                raise ValueError("La estructura del archivo JSON no coincide con la base de datos.")
        except json.JSONDecodeError:
            raise ValueError(f"El archivo {archivo} no tiene un formato JSON válido.")
        except Exception as e:
            raise IOError(f"Error al cargar usuarios desde {archivo}: {e}")

    def validar_estructura(self, data):
        required_keys = {"nombre", "email", "contrasena"}
        return all(isinstance(item, dict) and required_keys.issubset(item.keys()) for item in data)

    def login(self, email, contrasena):
        hash_input = self.hash_contrasena(contrasena)
        for usuario in self.usuarios:
            if usuario["email"] == email and usuario["contrasena"] == hash_input:
                return usuario
        return None
