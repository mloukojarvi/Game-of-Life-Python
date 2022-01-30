# Game-of-Life-Python
An implementation of Conway's Game of Life using Pygame

The game consists of a grid of cells that are either dead (0) or alive (1). At the beginning each cell is assigned a value randomly. At each time step each cell evolves according to the following rules:

1. Any live cell with two or three live neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead. 

In this implementation the walls of the grid are considered to be dead cells and they don't evolve. The dead cells are colored white and the live cells are colored black. Clicking with any mouse button restarts the game with new random values for the cells.

## Prerequisites
- Python 3
- Pygame

## Example Run
![game_of_life](https://user-images.githubusercontent.com/98547705/151698556-cbb2dbbb-2c65-4356-8466-99f68ac190ce.gif)
