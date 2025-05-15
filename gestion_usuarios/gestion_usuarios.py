import json
from decouple import config
from dotenv import load_dotenv
import os

load_dotenv()

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []
        self.default_file = config("DEFAULT_FILE", default=os.getenv("DEFAULT_FILE", "usuarios.json"))

    def registrar_usuario(self, nombre, email, contrasena):
        if not nombre or not email or not contrasena:
            print("Todos los campos son obligatorios.")
            return
        if "@" not in email or "." not in email:
            print("El email no tiene un formato válido.")
            return
        usuario = {
            "nombre": nombre,
            "email": email,
            "contrasena": contrasena
        }
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} registrado exitosamente.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for i, usuario in enumerate(self.usuarios, start=1):
                print(f"{i}. Nombre: {usuario['nombre']}, Email: {usuario['email']}")

    def buscar_usuario(self, nombre):
        resultados = [u for u in self.usuarios if nombre.lower() in u["nombre"].lower()]
        if resultados:
            print("Usuarios encontrados:")
            for i, usuario in enumerate(resultados, start=1):
                print(f"{i}. Nombre: {usuario['nombre']}, Email: {usuario['email']}")
            seleccion = input("Seleccione el número del usuario deseado o presione Enter para salir: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(resultados):
                usuario_seleccionado = resultados[int(seleccion) - 1]
                print(f"Usuario seleccionado: Nombre: {usuario_seleccionado['nombre']}, Email: {usuario_seleccionado['email']}")
            else:
                print("No se seleccionó ningún usuario.")
        else:
            print(f"No se encontraron usuarios con el nombre que contiene: {nombre}")

    def eliminar_usuario(self, nombre):
        resultados = [u for u in self.usuarios if nombre.lower() in u["nombre"].lower()]
        if resultados:
            print("Usuarios encontrados:")
            for i, usuario in enumerate(resultados, start=1):
                print(f"{i}. Nombre: {usuario['nombre']}, Email: {usuario['email']}")
            seleccion = input("Seleccione el número del usuario a eliminar o presione Enter para cancelar: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(resultados):
                usuario_seleccionado = resultados[int(seleccion) - 1]
                self.usuarios = [u for u in self.usuarios if u != usuario_seleccionado]
                print(f"✔️ Usuario {usuario_seleccionado['nombre']} eliminado exitosamente.")
            else:
                print("❌ No se seleccionó ningún usuario para eliminar.")
        else:
            print(f"❌ No se encontraron usuarios con el nombre que contiene: {nombre}")

    def guardar_usuarios(self, archivo=None):
        archivo = archivo or self.default_file
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(self.usuarios, f, ensure_ascii=False, indent=4)
            print(f"✔️ Usuarios guardados exitosamente en: {os.path.abspath(archivo)}")
        except Exception as e:
            print(f"❌ Error al guardar usuarios en {archivo}: {e}")

    def cargar_usuarios(self, archivo=None):
        print("Seleccione el tipo de archivo a cargar:")
        print("1. JSON")
        print("2. Excel")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            archivo = archivo or self.default_file
            if not os.path.exists(archivo):
                print(f"❌ El archivo {archivo} no existe. Se iniciará con una lista vacía.")
                return

            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if self.validar_estructura(data):
                    self.usuarios = data
                    print("✔️ Base de usuarios cargada desde JSON: OK")
                else:
                    print("❌ Error: La estructura del archivo JSON no coincide con la base de datos.")
            except json.JSONDecodeError:
                print(f"❌ Error: El archivo {archivo} no tiene un formato JSON válido.")
            except Exception as e:
                print(f"❌ Error al cargar usuarios desde {archivo}: {e}")

        elif opcion == "2":
            archivo = archivo or self.default_file
            import pandas as pd
            try:
                data = pd.read_excel(archivo).to_dict(orient="records")
                if self.validar_estructura(data):
                    self.usuarios = data
                    print("✔️ Base de usuarios cargada desde Excel: OK")
                else:
                    print("❌ Error: La estructura del archivo Excel no coincide con la base de datos.")
            except FileNotFoundError:
                print(f"❌ El archivo {archivo} no existe.")
            except Exception as e:
                print(f"❌ Error al cargar usuarios desde Excel: {e}")

        else:
            print("❌ Opción no válida. Intente nuevamente.")

        print("Ejemplo de archivo JSON:")
        print(json.dumps([{"nombre": "Juan Perez", "email": "juan.perez@example.com", "contrasena": "password123"}], indent=4, ensure_ascii=False))
        print("\nEjemplo de archivo Excel:")
        print("| nombre       | email                  | contrasena   |")
        print("|--------------|------------------------|--------------|")
        print("| Juan Perez   | juan.perez@example.com | password123  |")

    def validar_estructura(self, data):
        required_keys = {"nombre", "email", "contrasena"}
        return all(isinstance(item, dict) and required_keys.issubset(item.keys()) for item in data)
