from classes import *

def main():
    # Initialize the labyrinth from a text file
    labyrinth = Labyrinth('input.txt')
    labyrinth.print_labyrinth()

    # Initialize the rod with the starting coordinates and orientation
    rod = Rod(1, 0, 0)

    # Initialize the pathfinder
    pathfinder = Pathfinder(labyrinth, rod)

    # Run the BFS to find the shortest path
    print(pathfinder.perform_bfs())

if __name__ == "__main__":
    main()
