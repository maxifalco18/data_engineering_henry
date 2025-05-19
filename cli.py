from decouple import config
from gestion_usuarios.gestion_usuarios import GestionUsuarios
from colorama import Fore, Style, init
import os

DEFAULT_FILE = config('DEFAULT_FILE', default='usuarios_base.json')

init(autoreset=True)

def mostrar_menu():
    print(Fore.CYAN + "\nSistema de Gestión de Usuarios")
    print(Fore.GREEN + "1. Registrar usuario")
    print(Fore.GREEN + "2. Listar usuarios")
    print(Fore.GREEN + "3. Buscar usuario por nombre")
    print(Fore.GREEN + "4. Eliminar usuario")
    print(Fore.GREEN + "5. Guardar usuarios en archivo")
    print(Fore.GREEN + "6. Cargar usuarios desde archivo")
    print(Fore.YELLOW + "7. Login (Iniciar sesión)")
    print(Fore.RED + "8. Salir")

def main():
    print(f"Directorio de trabajo actual: {os.getcwd()}")
    gestion = GestionUsuarios()
    gestion.cargar_usuarios(DEFAULT_FILE)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            contrasena = input("Ingrese la contraseña: ")
            try:
                gestion.registrar_usuario(nombre, email, contrasena)
                print(Fore.GREEN + f"Usuario {nombre} registrado exitosamente.")
            except Exception as e:
                print(Fore.RED + str(e))
        elif opcion == "2":
            usuarios = gestion.listar_usuarios()
            if not usuarios:
                print(Fore.YELLOW + "No hay usuarios registrados.")
            else:
                for i, usuario in enumerate(usuarios, start=1):
                    print(f"{i}. Nombre: {usuario['nombre']}, Email: {usuario['email']}")
        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            resultados = gestion.buscar_usuario(nombre)
            if resultados:
                print(Fore.GREEN + "Usuarios encontrados:")
                for i, usuario in enumerate(resultados, start=1):
                    print(f"{i}. Nombre: {usuario['nombre']}, Email: {usuario['email']}")
            else:
                print(Fore.YELLOW + f"No se encontraron usuarios con el nombre que contiene: {nombre}")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del usuario a eliminar: ")
            try:
                usuario_eliminado = gestion.eliminar_usuario(nombre)
                print(Fore.GREEN + f"✔️ Usuario {usuario_eliminado['nombre']} eliminado exitosamente.")
            except Exception as e:
                print(Fore.RED + str(e))
        elif opcion == "5":
            archivo = input("Ingrese el nombre del archivo (con extensión .json) o presione Enter para cancelar: ")
            if not archivo.strip():
                print(Fore.YELLOW + "Operación cancelada. No se guardó ningún archivo.")
            else:
                try:
                    gestion.guardar_usuarios(archivo)
                    print(Fore.GREEN + f"✔️ Usuarios guardados exitosamente en: {os.path.abspath(archivo)}")
                except Exception as e:
                    print(Fore.RED + str(e))
        elif opcion == "6":
            archivo = input("Ingrese el nombre del archivo (con extensión .json) o presione Enter para usar el archivo por defecto: ")
            if not archivo.strip():
                archivo = DEFAULT_FILE
            try:
                gestion.cargar_usuarios(archivo)
                print(Fore.GREEN + "✔️ Base de usuarios cargada desde JSON: OK")
            except Exception as e:
                print(Fore.RED + str(e))
        elif opcion == "7":
            email = input("Ingrese su email: ")
            contrasena = input("Ingrese su contraseña: ")
            usuario = gestion.login(email, contrasena)
            if usuario:
                print(Fore.GREEN + f"Login exitoso. Bienvenido/a, {usuario['nombre']}!")
            else:
                print(Fore.RED + "Login fallido. Email o contraseña incorrectos.")
        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
