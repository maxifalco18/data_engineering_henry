import unittest
from gestion_usuarios.gestion_usuarios import GestionUsuarios

class TestGestionUsuarios(unittest.TestCase):

    def setUp(self):
        self.gestion = GestionUsuarios()

    def test_registrar_usuario(self):
        self.gestion.registrar_usuario("Juan", "juan@example.com", "password123")
        self.assertEqual(len(self.gestion.usuarios), 1)
        self.assertEqual(self.gestion.usuarios[0]["nombre"], "Juan")

    def test_buscar_usuario(self):
        self.gestion.registrar_usuario("Ana", "ana@example.com", "password123")
        resultados = [u for u in self.gestion.usuarios if u["nombre"].lower() == "ana"]
        self.assertEqual(len(resultados), 1)

    def test_eliminar_usuario(self):
        self.gestion.registrar_usuario("Luis", "luis@example.com", "password123")
        self.gestion.eliminar_usuario("Luis")
        self.assertEqual(len(self.gestion.usuarios), 0)

if __name__ == "__main__":
    unittest.main()
