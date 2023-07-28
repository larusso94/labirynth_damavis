import unittest
from classes import *

class TestRod(unittest.TestCase):
    def setUp(self):
        self.rod = Rod(1, 2, 0)

    def test_rod_initialization(self):
        self.assertEqual(self.rod.x_coordinate, 2)
        self.assertEqual(self.rod.y_coordinate, 1)
        self.assertEqual(self.rod.orientation, 0)


class TestLabyrinth(unittest.TestCase):
    def setUp(self):
        self.labyrinth = Labyrinth("input.txt")

    def test_labyrinth_initialization(self):
        self.assertEqual(self.labyrinth.num_rows, 5)
        self.assertEqual(self.labyrinth.num_columns, 9)


class TestPathfinder(unittest.TestCase):
    def setUp(self):
        self.rod = Rod(1, 2, 0)
        self.labyrinth = Labyrinth("input.txt")
        self.pathfinder = Pathfinder(self.labyrinth, self.rod)

    def test_move_valid(self):
        # Update the coordinates for valid move tests based on the labyrinth content
        self.assertFalse(self.pathfinder.is_move_valid(-1, -1, 0))  # Out of bounds
        self.assertTrue(self.pathfinder.is_move_valid(0, 2, 0))
        self.assertFalse(self.pathfinder.is_move_valid(0, 0, 0))  # Assuming there's a block here in the input.txt

    def test_corners_clear(self):
        # Update the coordinates for corners_clear tests based on the labyrinth content
        self.assertFalse(self.pathfinder.are_corners_clear(1, 1))
        self.assertTrue(self.pathfinder.are_corners_clear(1, 7))

    def test_rotation_possible(self):
        # Update the coordinates for rotation_possible tests based on the labyrinth content
        self.assertFalse(self.pathfinder.is_rotation_possible(1, 1, 1))
        self.assertTrue(self.pathfinder.is_rotation_possible(1, 7, 0))

    def test_perform_bfs(self):
        # Make sure you have a valid input.txt file with a valid path for this test
        self.assertNotEqual(self.pathfinder.perform_bfs(), -1)

if __name__ == "__main__":
    unittest.main()

