class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        index = 0
        value = nums[0]
        sum = 0
        count = 1

        while index + value < len(nums) - 1:
            for i in range(index + 1, index + 1 + nums[index]):
                if nums[i] + i >= sum:
                    index = i
                    value = nums[i]
                    sum = nums[i] + i
            count += 1

        return count


        