#!/usr/bin/python3

"""
ALX pascal's Triangle challenge
"""

def pascal_triangle(n):
    """
        Return a list of numbers fon Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # createthe first row of the triangle

    for i in range(1, n):
        row = [1]  # Each row starts with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle