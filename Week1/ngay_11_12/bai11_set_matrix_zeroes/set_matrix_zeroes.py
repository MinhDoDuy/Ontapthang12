from numpy.ma.extras import column_stack


class Solution:
    def zeroMatrix(self, matrix):
        cols, rows = set(), set()
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(i)
                    rows.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0