import argparse
from classes import *

def main():
    parser = argparse.ArgumentParser(description='Find the shortest path in a labyrinth.')
    parser.add_argument('file', type=str, help='Path to the input labyrinth file')
    args = parser.parse_args()

    # Initialize the labyrinth from the provided text file
    labyrinth = Labyrinth(args.file)
    labyrinth.print_labyrinth()

    # Initialize the rod with the starting coordinates and orientation
    rod = Rod()

    # Initialize the pathfinder
    pathfinder = Pathfinder(labyrinth, rod)

    # Run the BFS to find the shortest path
    print(pathfinder.perform_bfs())

if __name__ == "__main__":
    main()
