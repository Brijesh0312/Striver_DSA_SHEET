# O(m*n)
class Solution:
    def setColZero(self, i, matrix):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
        return matrix

    def setRowZero(self, j, matrix):
        for i in range(len(matrix)):
            matrix[i][j] = 0
        return matrix

    def setZeroes(self, matrix: List[List[int]]) -> None:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    ans.append([i, j])
        print(ans)
        for k in ans:
            matrix = self.setColZero(k[0], matrix)
            matrix = self.setRowZero(k[1], matrix)

#O(1)
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         ROWS = len(matrix)
#         COLS = len(matrix[0])
#         rowZero = False
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if (matrix[r][c] == 0):
#                     matrix[0][c] = 0
#                     if (r > 0):
#                         matrix[r][0] = 0
#                     else:
#                         rowZero = True
#         for r in range(1, ROWS):
#             for c in range(1, COLS):
#                 if (matrix[0][c] == 0 or matrix[r][0] == 0):
#                     matrix[r][c] = 0
#         if (matrix[0][0] == 0):
#             for r in range(ROWS):
#                 matrix[r][0] = 0
#         if rowZero:
#             for c in range(COLS):
#                 matrix[0][c] = 0
