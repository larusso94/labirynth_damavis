from collections import deque

class Rod:
    def __init__(self, y_coordinate=0, x_coordinate=1, orientation=0):
        """Initialize the rod with given position and orientation"""
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate
        self.orientation = orientation


class Labyrinth:
    def __init__(self, file):
        """Read the labyrinth layout from a given file"""
        try:
            with open(file, 'r') as f:
                self.grid = [list(line.strip()) for line in f]
        except IOError:
            print(f"Error: File {file} not found.")
            return None

        self.num_rows, self.num_columns = len(self.grid), len(self.grid[0])

    def print_labyrinth(self):
        """Print the labyrinth layout"""
        print('Number of rows:', self.num_rows, 'Number of columns:', self.num_columns)
        for row in self.grid:
            print(''.join(row))


class Pathfinder:
    # Define movement directions
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self, labyrinth, rod):
        """Initialize the pathfinder with given labyrinth and rod"""
        self.labyrinth = labyrinth
        self.rod = rod

        # Initialize the visited array and queue for the BFS traversal
        self.visited = [[[False for _ in range(self.labyrinth.num_columns)] for _ in range(self.labyrinth.num_rows)] for _ in range(2)]
        self.queue = deque()

    def is_end_of_labyrinth(self, y, x, orientation):
        """Check if the current position is the end of the labyrinth"""
        return (orientation == 0 and x == self.labyrinth.num_columns - 2 and y == self.labyrinth.num_rows - 1) or \
               (orientation == 1 and x == self.labyrinth.num_columns - 1 and y == self.labyrinth.num_rows - 2)

    def is_move_valid(self, new_y, new_x, orientation):
        """Check if the new position is valid"""
        grid = self.labyrinth.grid

        # Return False if the new position is out of bounds
        if new_x < 0 or new_x >= self.labyrinth.num_columns or new_y < 0 or new_y >= self.labyrinth.num_rows:
            return False

        # Check if the new position goes outside the labyrinth when rotating
        if (orientation == 0 and (new_x - 1 < 0 or new_x + 1 >= self.labyrinth.num_columns)) or \
           (orientation == 1 and (new_y - 1 < 0 or new_y + 1 >= self.labyrinth.num_rows)):
            return False

        # Return False if the new position is already visited or blocked
        if self.visited[orientation][new_y][new_x] or grid[new_y][new_x] == '#':
            return False

        # Check the validity of the move based on the rod's orientation
        if (orientation == 0 and (grid[new_y][new_x - 1] == '#' or grid[new_y][new_x + 1] == '#')) or \
           (orientation == 1 and (grid[new_y - 1][new_x] == '#' or grid[new_y + 1][new_x] == '#')):
            return False

        return True

    def are_corners_clear(self, y, x):
        """Check the corners for blocks to determine if the rod can rotate"""
        if x - 1 < 0 or y - 1 < 0 or x + 1 >= self.labyrinth.num_columns or y + 1 >= self.labyrinth.num_rows or \
           self.labyrinth.grid[y - 1][x] == '#' or self.labyrinth.grid[y + 1][x] == '#' or \
           self.labyrinth.grid[y][x - 1] == '#' or self.labyrinth.grid[y][x + 1] == '#':
            return False

        return True

    def is_rotation_possible(self, y, x, orientation):
        """Check if rotation is possible"""
        # Both the corners are clear and the move is valid with the new orientation
        return self.are_corners_clear(y, x) and self.is_move_valid(y, x, 1 - orientation)

    def perform_bfs(self):
        """Perform BFS traversal"""
        self.queue.append((self.rod.y_coordinate, self.rod.x_coordinate, self.rod.orientation, 0))
        self.visited[self.rod.orientation][self.rod.y_coordinate][self.rod.x_coordinate] = True

        while self.queue:
            y, x, orientation, moves = self.queue.popleft()

            if self.is_end_of_labyrinth(y, x, orientation):
                return moves

            for dx, dy in self.DIRECTIONS:
                new_y, new_x = y + dy, x + dx
                if not self.is_move_valid(new_y, new_x, orientation):
                    continue

                self.visited[orientation][new_y][new_x] = True
                self.queue.append((new_y, new_x, orientation, moves + 1))

            if self.is_rotation_possible(y, x, orientation):
                orientation = 1 - orientation
                self.visited[orientation][y][x] = True
                self.queue.append((y, x, orientation, moves + 1))

        return -1
