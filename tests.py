import unittest

class TestPathfinder(unittest.TestCase):
    def setUp(self):
        self.labyrinth = Labyrinth('labyrinth.txt')  # Assuming that labyrinth.txt is a valid file
        self.rod = Rod(1, 0, 0)
        self.pathfinder = Pathfinder(self.labyrinth, self.rod)

    def test_labyrinth_end(self):
        # Test case: end of labyrinth for horizontal rod
        self.assertEqual(self.pathfinder.labyrinth_end(self.labyrinth.n-1, self.labyrinth.m-1, 0), True)
        # Test case: not end of labyrinth for horizontal rod
        self.assertEqual(self.pathfinder.labyrinth_end(self.labyrinth.n-1, self.labyrinth.m-2, 0), False)
        # Test case: end of labyrinth for vertical rod
        self.assertEqual(self.pathfinder.labyrinth_end(self.labyrinth.n-2, self.labyrinth.m-1, 1), True)
        # Test case: not end of labyrinth for vertical rod
        self.assertEqual(self.pathfinder.labyrinth_end(self.labyrinth.n-2, self.labyrinth.m-2, 1), False)

    def test_valid_move(self):
        # Test case: inside boundaries and free space
        self.assertEqual(self.pathfinder.valid_move(1, 1, 0), 1)
        # Test case: outside boundaries
        self.assertEqual(self.pathfinder.valid_move(self.labyrinth.n, self.labyrinth.m, 0), 0)
        # Test case: occupied space
        self.pathfinder.labyrinth.grid[1][1] = '#'
        self.assertEqual(self.pathfinder.valid_move(1, 1, 0), 0)
        # Test case: visited space
        self.pathfinder.visited[0][1][1] = True
        self.assertEqual(self.pathfinder.valid_move(1, 1, 0), 0)

    def test_check_corners(self):
        # Test case: free corners
        self.assertEqual(self.pathfinder.check_corners(2, 2), 1)
        # Test case: top left corner occupied
        self.pathfinder.labyrinth.grid[1][1] = '#'
        self.assertEqual(self.pathfinder.check_corners(2, 2), 0)

    def test_can_rotate(self):
        # Test case: can rotate
        self.assertEqual(self.pathfinder.can_rotate(2, 2, 0), 1)
        # Test case: cannot rotate
        self.pathfinder.labyrinth.grid[1][2] = '#'
        self.assertEqual(self.pathfinder.can_rotate(2, 2, 0), 0)

    def test_bfs(self):
        moves = self.pathfinder.bfs()
        # Test if the returned moves is integer
        self.assertIsInstance(moves, int)
        # Test if the number of moves is -1 or more (meaning that the end was reached)
        self.assertTrue(moves >= -1)

if __name__ == '__main__':
    unittest.main()
