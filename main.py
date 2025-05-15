from gestion_usuarios.gestion_usuarios import GestionUsuarios
from colorama import Fore, Style, init
import os

init(autoreset=True)

def main():
    print(f"Directorio de trabajo actual: {os.getcwd()}")  # Debug statement
    gestion = GestionUsuarios()
    gestion.cargar_usuarios("C:/Users/CTI23994/Dropbox/Data Engineering - HENRY/proyecto_final/usuarios_base.json")

    while True:
        print(Fore.CYAN + "\nSistema de Gestión de Usuarios")
        print(Fore.GREEN + "1. Registrar usuario")
        print(Fore.GREEN + "2. Listar usuarios")
        print(Fore.GREEN + "3. Buscar usuario por nombre")
        print(Fore.GREEN + "4. Eliminar usuario")
        print(Fore.GREEN + "5. Guardar usuarios en archivo")
        print(Fore.GREEN + "6. Cargar usuarios desde archivo")
        print(Fore.RED + "7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            email = input("Ingrese el email: ")
            contrasena = input("Ingrese la contraseña: ")
            gestion.registrar_usuario(nombre, email, contrasena)
        elif opcion == "2":
            gestion.listar_usuarios()
        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            gestion.buscar_usuario(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del usuario a eliminar: ")
            gestion.eliminar_usuario(nombre)
        elif opcion == "5":
            archivo = input("Ingrese el nombre del archivo (con extensión .json): ")
            gestion.guardar_usuarios(archivo)
        elif opcion == "6":
            archivo = input("Ingrese el nombre del archivo (con extensión .json): ")
            gestion.cargar_usuarios(archivo)
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
