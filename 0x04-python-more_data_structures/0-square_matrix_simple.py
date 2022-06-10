#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMat = []
    for row in matrix:
        newRow = list([x**2 for x in row])
        newMat.append(newRow)
    return newMat
