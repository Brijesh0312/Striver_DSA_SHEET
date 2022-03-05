#O(numRows*numRows)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows == 1):
            return [[1]]
        elif (numRows == 2):
            return [[1], [1, 1]]
        pascalTriangle = [[1], [1, 1]]
        numRows -= 2
        i = 1
        lst = []
        while (numRows):
            lst.append(1)

            for j in range(0, len(pascalTriangle[i]) - 1):
                lst.append(pascalTriangle[i][j] + pascalTriangle[i][j + 1])
            lst.append(1)
            pascalTriangle.append(lst)
            lst = []
            i += 1
            numRows -= 1
        return pascalTriangle

