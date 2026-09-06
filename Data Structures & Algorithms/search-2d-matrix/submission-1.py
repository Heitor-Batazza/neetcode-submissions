class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(0, len(matrix)):
            if target >= matrix[i][0]:
                row = i
        for j in range(0, len(matrix[row])):
            if target == matrix[row][j]:
                return True
        return False
        
        