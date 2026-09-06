class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r, r_r = 0, len(matrix) - 1
        l_c, r_c = 0, len(matrix[0]) - 1


        while l_r <= r_r:
            m = (l_r + r_r) // 2

            if target > matrix[m][0] and (m + 1 not in range(len(matrix)) or target < matrix[m + 1][0]):
                break

            elif target > matrix[m][0]:
                l_r = m + 1
            
            elif target < matrix[m][0]:
                r_r = m - 1

            else:
                return True

        while l_c <= r_c:
            n = (l_c + r_c) // 2

            if target > matrix[m][n]:
                l_c = n + 1
            
            elif target < matrix[m][n]:
                r_c = n - 1

            else:
                return True

        return False

        