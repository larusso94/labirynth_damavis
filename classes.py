from collections import deque

class Rod:
    def __init__(self, x=1, y=0, orientation = 0):
        # Defines the initial position and orientation of the rod
        self.y = y
        self.x = x
        self.orientation = orientation

class Labyrinth:
    def __init__(self, file):
        # Opens the file and reads the labyrinth layout
        with open(file, 'r') as f:
            self.grid = [list(line.strip()) for line in f]
        self.n, self.m = len(self.grid), len(self.grid[0])

    def print_labyrinth(self):
        # Prints the labyrinth layout
        for row in self.grid:
            print(''.join(row))

class Pathfinder:
    def __init__(self, labyrinth, rod):
        self.labyrinth = labyrinth
        self.rod = rod

        # Initializes the visited array and queue for the BFS traversal
        self.visited = [[[False for _ in range(self.labyrinth.m)] for _ in range(self.labyrinth.n)] for _ in range(2)]
        self.queue = deque()
        
        # Defines the movement directions
        self.dx = [0, 1, 0, -1]
        self.dy = [-1, 0, 1, 0]

    def is_end_of_labyrinth(self, y, x, orientation):
        # Checks if the current position is the end of the labyrinth
        return (orientation == 0 and x+1 == self.labyrinth.m-1 and y == self.labyrinth.n-1) or (orientation == 1 and x == self.labyrinth.m-1 and y+1 == self.labyrinth.n-1)
    
    def is_move_valid(self, ny, nx, orientation):
        grid = self.labyrinth.grid
        
        if nx - 1 < 0 or nx + 1 >= self.labyrinth.m or ny - 1 < 0 or ny + 1 >= self.labyrinth.n :
            return False
        
        # Returns false if the new position is already visited or blocked
        if self.visited[orientation][ny][nx] or grid[ny][nx] == '#' or nx < 0 or nx >= self.labyrinth.m or ny < 0 or ny >= self.labyrinth.n:
            return False

        # Checks the validity of the move based on the rod's orientation
        if (orientation == 0 and (grid[ny][nx - 1] == '#'  or grid[ny][nx + 1] == '#')) or (orientation == 1 and ( grid[ny - 1][nx] == '#'  or grid[ny + 1][nx] == '#')):
            return False
        
        return True

    def are_corners_clear(self, y, x):
        # Checks the corners for blocks in order to determine if the rod can rotate
        if x - 1 < 0 or y - 1 < 0 or x + 1 >= self.labyrinth.n or y + 1 >= self.labyrinth.m or self.labyrinth.grid[y - 1][x - 1] == '#' or self.labyrinth.grid[y + 1][x + 1] == '#' or self.labyrinth.grid[y - 1][x + 1] == '#' or self.labyrinth.grid[y + 1][x - 1] == '#':
            return False
        
        return True

    def is_rotation_possible(self, y, x, orientation):
        # Returns true if rotation is possible, i.e., both the corners are clear and the move is valid with the new orientation
        return self.are_corners_clear(y, x) and self.is_move_valid(y, x, 1 - orientation)

    def perform_bfs(self):
        # Starts the BFS traversal
        self.queue.append((self.rod.y, self.rod.x, self.rod.orientation, 0))
        self.visited[self.rod.orientation][self.rod.y][self.rod.x] = True


        while self.queue:
            y, x, orientation, moves = self.queue.popleft()
            
            if self.is_end_of_labyrinth(y,x,orientation):
                print(x, y, orientation)
                return moves
            
            for i in range(4):
                ny, nx = y + self.dy[i], x + self.dx[i]

                if not self.is_move_valid(ny, nx, orientation):
                    continue
                
                self.visited[orientation][ny][nx] = True
                self.queue.append((ny, nx, orientation, moves + 1))
            
            if self.is_rotation_possible(y, x, orientation):
                orientation = 1 - orientation
                self.visited[orientation][y][x] = True
                self.queue.append((y, x, orientation, moves + 1))

        return -1
