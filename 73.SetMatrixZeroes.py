# Time Complexity: O(N)
# Space Complexity: O(N)
# N: number of element in the matrix

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        pList = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    pList.append((i, j))
        for p in pList:
            for i in range(len(matrix[0])):
                matrix[p[0]][i] = 0
        for p in pList:
            for i in range(len(matrix)):
                matrix[i][p[1]] = 0
