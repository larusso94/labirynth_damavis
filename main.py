import argparse
from classes import *

def main():
    parser = argparse.ArgumentParser(description='Find the shortest path in a labyrinth.')
    parser.add_argument('file', type=str, help='Path to the input labyrinth file')
    args = parser.parse_args()

    # Initialize the labyrinth from the provided text file
    try:
        labyrinth = Labyrinth(args.file)
    except IOError:
        print(f"Error: File {args.file} not found.")
        return

    labyrinth.print_labyrinth()

    # Initialize the rod with the starting coordinates and orientation
    rod = Rod()

    # Initialize the pathfinder
    pathfinder = Pathfinder(labyrinth, rod)

    # Run the BFS to find the shortest path
    shortest_path_length = pathfinder.perform_bfs()
    if shortest_path_length == -1:
        print("No valid path was found.")
    else:
        print("The shortest path length is:", shortest_path_length)

if __name__ == "__main__":
    main()
