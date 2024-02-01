################################################################################
# 
# Computing Basics / Fundamentos de Informática
# University of Oviedo / Universidad de Oviedo
#
# Copyright (c) 2022 Javier Escalada Gómez
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
###

def zeros(rows, cols):
    """
    >>> zeros(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    matrix = []
    for y in range(rows):
        matrix.append([0]*cols)
    return matrix


def identity(n):
    """
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    matrix = zeros(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def is_matrix(m):
    """
    >>> is_matrix([[1, 2], [3, 4]])
    True
    >>> is_matrix([[1, 2], [3, 4, 5]])
    False
    >>> is_matrix([[1, 2], [3, 4], [5, 6]])
    True
    """
    if len(m) == 0:
        return False
    cols = len(m[0])
    for row in m:
        if len(row) != cols:
            return False
    return True


def shape(m):
    """
    >>> shape([[1, 2], [3, 4]])
    (2, 2)
    >>> shape([[1, 2], [3, 4], [5, 6]])
    (3, 2)
    >>> shape([[1, 2], [3]])
    (None, None)
    """
    if not is_matrix(m):
        return None, None
    rows = len(m)
    cols = len(m[0])
    return rows, cols


def transpose(m):
    """
    >>> transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    if not is_matrix(m):
        return None
    rows, cols = shape(m)
    matrix = zeros(cols, rows)
    for y in range(rows):
        for x in range(cols):
            matrix[x][y] = m[y][x]
    return matrix


def add(m1, m2):
    """
    >>> add([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[6, 8], [10, 12]]
    >>> add([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
    """
    if not is_matrix(m1) or not is_matrix(m2) or shape(m1) != shape(m2):
        return None
    rows, cols = shape(m1)
    matrix = zeros(rows, cols)
    for y in range(rows):
        for x in range(cols):
            matrix[y][x] = m1[y][x] + m2[y][x]
    return matrix


def matmul(m1, m2):
    """
    >>> matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matmul([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
    """
    if not is_matrix(m1) or not is_matrix(m2) or shape(m1)[1] != shape(m2)[0]:
        return None
    rows, cols = shape(m1)
    matrix = zeros(rows, cols)
    for y in range(rows):
        for x in range(cols):
            for i in range(cols):
                matrix[y][x] += m1[y][i] * m2[i][x]
    return matrix


def scalmul(s, m):
    """
    >>> scalmul(2, [[1, 2], [3, 4]])
    [[2, 4], [6, 8]]
    """
    if not is_matrix(m):
        return None
    rows, cols = shape(m)
    matrix = zeros(rows, cols)
    for y in range(rows):
        for x in range(cols):
            matrix[y][x] = s * m[y][x]
    return matrix


def sub(m1, m2):
    """
    >>> sub([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[-4, -4], [-4, -4]]
    >>> sub([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
    """
    return add(m1, scalmul(-1, m2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()