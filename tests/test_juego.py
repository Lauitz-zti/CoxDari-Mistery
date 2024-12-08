import unittest
from unittest.mock import patch
from juego.juego import mover_personaje, interactuar, abrir_menu, abrir_inventario, personaje, inventario
import sys
import time

class TestJuego(unittest.TestCase):
    # Test para mover_personaje
    def test_mover_personaje(self):
        global personaje
        personaje = {"x": 0, "y": 0}  # Restablecer personaje antes de la prueba
        mover_personaje("w")
        self.assertEqual(personaje["y"], 1)

        mover_personaje("s")
        self.assertEqual(personaje["y"], 0)

        mover_personaje("a")
        self.assertEqual(personaje["x"], -1)

        mover_personaje("d")
        self.assertEqual(personaje["x"], 0)

    # Test para interactuar
    @patch('builtins.print')
    def test_interactuar(self, mock_print):
        interactuar()
        mock_print.assert_called_with("Has interactuado con un objeto o personaje cercano.")

    # Test para abrir_menu
    @patch('builtins.print')
    @patch('time.sleep', return_value=None)  # Para evitar la espera
    def test_abrir_menu(self, mock_sleep, mock_print):
        abrir_menu()
        mock_print.assert_any_call("Menú del juego abierto. Pulsa 'ESC' nuevamente para cerrarlo.")
        mock_print.assert_any_call("Menú cerrado.")

    # Test para abrir_inventario vacío
    @patch('builtins.print')
    @patch('time.sleep', return_value=None)  # Para evitar la espera
    def test_abrir_inventario_vacio(self, mock_sleep, mock_print):
        global inventario
        inventario = []  # Inventario vacío
        abrir_inventario()
        mock_print.assert_any_call("Inventario abierto:")
        mock_print.assert_any_call("Tu inventario está vacío.")
        mock_print.assert_any_call("Inventario cerrado.")

    # Test para abrir_inventario con elementos
    @patch('builtins.print')
    @patch('time.sleep', return_value=None)  # Para evitar la espera
    def test_abrir_inventario_con_items(self, mock_sleep, mock_print):
        global inventario
        inventario = ["Espada", "Escudo"]
        abrir_inventario()
        mock_print.assert_any_call("Inventario abierto:")
        mock_print.assert_any_call("1. Espada")
        mock_print.assert_any_call("2. Escudo")
        mock_print.assert_any_call("Inventario cerrado.")

# Ejecutar los tests
if __name__ == '__main__':
    unittest.main()
