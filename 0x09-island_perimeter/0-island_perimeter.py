#!/usr/bin/python3

"""
Calculate the perimeter of the island described in the grid.

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
"""


def island_perimeter(grid):
    """
        Find the primeter of the island
    """
    rows = len(grid)
    columns = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:  # If the cell is a land cell
                # Start with 4 sides
                cell_perimeter = 4

                # Check above it
                if i > 0 and grid[i - 1][j] == 1:
                    cell_perimeter -= 1

                # Check the below
                if i < rows - 1 and grid[i + 1][j] == 1:
                    cell_perimeter -= 1

                # Check the left
                if j > 0 and grid[i][j - 1] == 1:
                    cell_perimeter -= 1

                # Check the right
                if j < columns - 1 and grid[i][j + 1] == 1:
                    cell_perimeter -= 1

                # Add to total perimeter
                perimeter += cell_perimeter

    return perimeter
