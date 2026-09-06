class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_unicas = set(nums)
        for i in range(0, len(nums)):
            if nums[i] in nums_unicas:
                nums_unicas.remove(nums[i])
            else:
                return True
        return False