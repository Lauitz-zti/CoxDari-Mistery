import unittest
from pymongo import MongoClient
from include import crear_usuario, agregar_personaje_secundario, agregar_reto, agregar_item, agregar_pista  # Importación desde biblioteca

class TestMongoDBConexion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuración inicial de prueba (usar base de datos de prueba)
        cls.client = MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client['test_CoxDariMysteri']  # Base de datos de prueba

        # Colecciones
        cls.usuarios = cls.db['usuarios']
        cls.personajes_secundarios = cls.db['personajes_secundarios']
        cls.retos_misiones = cls.db['retos_misiones']
        cls.items = cls.db['items']
        cls.pistas = cls.db['pistas']

    @classmethod
    def tearDownClass(cls):
        # Limpieza: Elimina la base de datos de prueba
        cls.client.drop_database('test_CoxDariMysteri')

    def test_crear_usuario(self):
        crear_usuario("TestUser", "avatar.png", nivel=5)
        usuario = self.usuarios.find_one({"nombre": "TestUser"})
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nivel"], 5)

    def test_agregar_personaje_secundario(self):
        agregar_personaje_secundario("TestCharacter", "Python", "Stealth", ["pista1"])
        personaje = self.personajes_secundarios.find_one({"nombre": "TestCharacter"})
        self.assertIsNotNone(personaje)
        self.assertEqual(personaje["lenguaje_programacion"], "Python")

    def test_agregar_reto(self):
        agregar_reto("TestChallenge", "Logical test", "Python", "SolutionCode", "Hard", 100, "2h", "Level 3")
        reto = self.retos_misiones.find_one({"nombre": "TestChallenge"})
        self.assertIsNotNone(reto)
        self.assertEqual(reto["dificultad"], "Hard")

    def test_agregar_item(self):
        agregar_item("TestItem", "A test item", "Utility", "Boost")
        item = self.items.find_one({"nombre": "TestItem"})
        self.assertIsNotNone(item)
        self.assertEqual(item["efecto"], "Boost")

    def test_agregar_pista(self):
        agregar_pista("Test Clue", "TestCharacter", "TestChallenge")
        pista = self.pistas.find_one({"descripcion": "Test Clue"})
        self.assertIsNotNone(pista)
        self.assertEqual(pista["personaje_asociado"], "TestCharacter")

if __name__ == "__main__":
    unittest.main()
