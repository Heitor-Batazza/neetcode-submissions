class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += num
            output = max(output, curSum)

        return output

        