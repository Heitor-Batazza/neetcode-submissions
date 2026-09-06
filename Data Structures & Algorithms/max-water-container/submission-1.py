class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        p, q = 0, (len(heights) - 1)

        while p != q:
            Area = min(heights[p], heights[q]) * (q - p)
            output = max(Area, output)
            if heights[q] >= heights[p]:
                p = p + 1
            else:
                q = q - 1
        
        return output

        