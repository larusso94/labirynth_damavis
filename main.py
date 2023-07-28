from classes import *

# usage
rod = Rod(x=1,y=0,orientation=0)

labyrinth = Labyrinth('input.txt')

labyrinth.print_labyrinth()

pathfinder = Pathfinder(labyrinth, rod)

print(pathfinder.bfs())