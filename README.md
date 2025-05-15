# Sistema de Gestión de Usuarios

Este proyecto es una aplicación en Python que permite gestionar usuarios mediante un sistema modularizado. Las funcionalidades incluyen:

- Registrar usuarios (nombre, email, contraseña).
- Listar usuarios registrados.
- Buscar usuarios por nombre.
- Eliminar usuarios.
- Guardar y cargar la lista de usuarios en archivos externos (`.json`).

## Requisitos

- Python 3.7 o superior.

## Configuración del Entorno Virtual

1. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

2. Activar el entorno virtual:

   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
proyecto_final/
│
├── gestion_usuarios/          # Módulo principal
│   ├── __init__.py            # Indica que es un paquete Python
│   ├── gestion_usuarios.py    # Lógica principal de gestión de usuarios
│
├── tests/                     # Pruebas unitarias
│   ├── __init__.py            # Indica que es un paquete Python
│   ├── test_gestion_usuarios.py  # Pruebas para la lógica de usuarios
│
├── main.py                    # Punto de entrada principal del programa
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación del proyecto
├── .env                       # Variables de entorno
```

## Ejecución

1. Asegúrese de que el entorno virtual esté activado.
2. Ejecute el archivo principal:

   ```bash
   python main.py
   ```

## Pruebas Unitarias

1. Asegúrese de que el entorno virtual esté activado.
2. Ejecute las pruebas unitarias:

   ```bash
   python -m unittest discover tests
   ```

## Mejoras Implementadas

### Uso de Variables de Entorno
- Se utiliza `python-decouple` y `python-dotenv` para manejar configuraciones sensibles desde un archivo `.env`.

### Validaciones Robustas
- Validación del formato de email al registrar usuarios.
- Verificación de campos obligatorios.

### Manejo de Errores
- Uso de `try/except` para manejar errores al cargar y guardar archivos JSON.

### Mejoras Visuales
- Se utiliza `colorama` para mejorar la experiencia visual en la consola con colores para opciones y mensajes.

### Modularización
- El proyecto está organizado en módulos (`gestion_usuarios`) y pruebas (`tests`) para facilitar el mantenimiento y la escalabilidad.

## Notas

- Asegúrese de que los archivos `.json` utilizados para guardar/cargar usuarios tengan el formato correcto.
- Si tiene preguntas o problemas, no dude en contactarme.
