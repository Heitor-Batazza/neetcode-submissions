class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1, 0, -1):
            for j in range(0, i):
                if (nums[j] + nums[i]) == target:
                    return [j,i]