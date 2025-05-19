import unittest
from gestion_usuarios.gestion_usuarios import GestionUsuarios

class TestGestionUsuarios(unittest.TestCase):
    def setUp(self):
        self.gestion = GestionUsuarios()

    def test_registrar_usuario_hash(self):
        usuario = self.gestion.registrar_usuario("Juan", "juan@example.com", "password123")
        self.assertEqual(len(self.gestion.usuarios), 1)
        self.assertNotEqual(usuario["contrasena"], "password123")
        self.assertEqual(len(usuario["contrasena"]), 64)  # SHA-256 hash length

    def test_login_exitoso(self):
        self.gestion.registrar_usuario("Ana", "ana@example.com", "password123")
        usuario = self.gestion.login("ana@example.com", "password123")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nombre"], "Ana")

    def test_login_fallido(self):
        self.gestion.registrar_usuario("Luis", "luis@example.com", "password123")
        usuario = self.gestion.login("luis@example.com", "wrongpass")
        self.assertIsNone(usuario)
        usuario = self.gestion.login("noexiste@example.com", "password123")
        self.assertIsNone(usuario)

    def test_buscar_usuario(self):
        self.gestion.registrar_usuario("Ana", "ana@example.com", "password123")
        resultados = self.gestion.buscar_usuario("ana")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["nombre"], "Ana")

    def test_eliminar_usuario(self):
        self.gestion.registrar_usuario("Luis", "luis@example.com", "password123")
        eliminado = self.gestion.eliminar_usuario("Luis")
        self.assertEqual(eliminado["nombre"], "Luis")
        self.assertEqual(len(self.gestion.usuarios), 0)

    def test_listar_usuarios(self):
        self.gestion.registrar_usuario("Laura", "laura@example.com", "password123")
        lista = self.gestion.listar_usuarios()
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0]["nombre"], "Laura")
        self.assertNotIn("contrasena", lista[0])

if __name__ == "__main__":
    unittest.main()
