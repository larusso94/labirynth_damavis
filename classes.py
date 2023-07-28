from collections import deque

class Rod:
    def __init__(self, x=1, y=0, orientation = 0):
        self.y = y  # y-coordinate of the center of the rod
        self.x = x  # x-coordinate of the center of the rod
        self.orientation = orientation  # 0 for horizontal, 1 for vertical

class Labyrinth:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.grid = [list(line.strip()) for line in f]  # Reads the labyrinth from a text file and converts it into a 2D list
        self.n, self.m = len(self.grid), len(self.grid[0])  # Dimensions of the labyrinth n=filas, m=colunmnas
        print('Filas ',self.n,'Columnas ',self.m)

    def print_labyrinth(self):
        for row in self.grid:  # Iterates through each row of the labyrinth
            print(''.join(row))  # Prints the row as a string

class Pathfinder:
    def __init__(self, labyrinth, rod):
        self.labyrinth = labyrinth  # Labyrinth object, represents the maze
        self.rod = rod  # Rod object, represents the rod that needs to be moved
        # 4-dimensional visited array, keeps track of the cells visited with each orientation
        self.visited = [[[False for _ in range(self.labyrinth.m)] for _ in range(self.labyrinth.n)] for _ in range(2)]
        self.queue = deque()  # Queue for BFS traversal
        # Change in x for each direction: up, right, down, left
        self.dx = [0, 1, 0, -1]  
        # Change in y for each direction: up, right, down, left
        self.dy = [-1, 0, 1, 0]

    def valid_move(self, ny, nx, orientation):
        if orientation == 0 and (nx < 0 or nx >= self.labyrinth.m or ny < 0 or ny >= self.labyrinth.n):
            return 0
        if orientation == 1 and (nx < 0 or nx >= self.labyrinth.m or ny < 0 or ny >= self.labyrinth.n):
            return 0
        return 1
    
    def labyrinth_end(self, y, x, orientation):
        return (orientation == 0 and x+1 == self.labyrinth.m-1 and y == self.labyrinth.n-1) or (orientation == 1 and x == self.labyrinth.m-1 and y+1 == self.labyrinth.n-1)

    def bfs(self):
        # Insert the initial position (center of the rod) into the queue. 
        # The fourth value in the tuple is the number of moves, which is 0 at the start.
        self.queue.append((self.rod.y, self.rod.x, self.rod.orientation, 0)) 
        self.visited[self.rod.orientation][self.rod.y][self.rod.x] = True

        # Continue as long as there are elements in the queue
        while self.queue:
            # Pop the first element from the queue. This gives us the current position (x, y), 
            # orientation, and number of moves made to reach there.
            y, x, orientation, moves = self.queue.popleft()
            grid = self.labyrinth.grid
            
            # If so, return the number of moves made so far.
            if self.labyrinth_end(y,x,orientation):
                return moves
            
            # Try to move in all four directions from the current position
            for i in range(4):
                ny, nx  =y + self.dy[i], x + self.dx[i]   # Calculate the new position

                # Check if one end of the rod is at the bottom-right corner of the grid (destination)
                if not self.valid_move(ny, nx, orientation):
                    continue

                if grid[ny][nx] == '#':
                    continue
                
                # Check if the new position is not a wall and the space for rotation is clear
                if orientation == 0:
                    if nx - 1 < 0 or grid[ny][nx - 1] == '#':
                        continue
                    if nx + 1 >= self.labyrinth.m or grid[ny][nx + 1] == '#':
                        continue
                else:
                    if ny - 1 < 0 or grid[ny - 1][nx] == '#':
                        continue
                    if ny + 1 >= self.labyrinth.n or grid[ny + 1][nx] == '#':
                        continue
                
                # If we've visited this position before with the same orientation, skip this direction
                if self.visited[orientation][ny][nx]:
                    continue
                
                # Mark the new position as visited
                self.visited[orientation][ny][nx] = True
                
                # Add the new position to the queue, with the same orientation and an incremented move count
                self.queue.append((ny, nx, orientation, moves + 1))

            # Rotate the rod, changing its orientation
            orientation = 1 - orientation

            # Check if the rod would hit the wall after rotation, if so, skip this direction
            if (orientation == 0 and (x+1 >= self.labyrinth.m or x-1 <= 0)) or (orientation == 1 and x == (y+1 >= self.labyrinth.n or y-1 <= 0)):
                continue

            # If we've visited this position before with the new orientation, skip this direction
            if self.visited[orientation][y][x]:
                continue

            # Mark the position as visited with the new orientation
            self.visited[orientation][y][x] = True
            
            # Add the current position to the queue, but with the new orientation and an incremented move count
            self.queue.append((y, x, orientation, moves + 1))

        # If no valid path was found, return -1
        return -1


