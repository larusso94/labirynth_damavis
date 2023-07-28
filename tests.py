from classes import *
import unittest

class TestRod(unittest.TestCase):
    def setUp(self):
        self.rod = Rod(1, 2, 0)

    def test_rod_initialization(self):
        self.assertEqual(self.rod.x, 1)
        self.assertEqual(self.rod.y, 2)
        self.assertEqual(self.rod.orientation, 0)

class TestLabyrinth(unittest.TestCase):
    def setUp(self):
        # Aquí utilizamos un archivo ficticio "test_file.txt", asegúrate de cambiarlo a un archivo válido en tu entorno.
        self.labyrinth = Labyrinth("input.txt")

    def test_labyrinth_initialization(self):
        # Aquí suponemos que "test_file.txt" es un archivo con una cuadrícula de 3x3. Cambia estos valores según corresponda.
        self.assertEqual(self.labyrinth.n, 3)
        self.assertEqual(self.labyrinth.m, 3)

class TestPathfinder(unittest.TestCase):
    def setUp(self):
        self.rod = Rod(1, 2, 0)
        self.labyrinth = Labyrinth("input.txt")
        self.pathfinder = Pathfinder(self.labyrinth, self.rod)

    def test_move_valid(self):
        self.assertFalse(self.pathfinder.is_move_valid(-1, -1, 0))  # Fuera de límites
        self.assertTrue(self.pathfinder.is_move_valid(0,2,0))
        self.assertFalse(self.pathfinder.is_move_valid(0, 0, 0))  # Suponiendo que hay un bloque aquí en "test_file.txt"

    def test_corners_clear(self):
        # Asegúrate de establecer la posición a una que tenga todos los rincones libres
        self.assertTrue(self.pathfinder.are_corners_clear(1, 1))

    def test_rotation_possible(self):
        # Asegúrate de establecer la posición a una que pueda rotar
        self.assertTrue(self.pathfinder.is_rotation_possible(1, 1, 0))

    def test_perform_bfs(self):
        # Si la función perform_bfs no puede encontrar una ruta válida, devuelve -1
        self.assertNotEqual(self.pathfinder.perform_bfs(), -1)

if __name__ == "__main__":
    unittest.main()