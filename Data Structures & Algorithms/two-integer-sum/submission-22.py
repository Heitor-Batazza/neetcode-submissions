class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, value in enumerate(nums):
            if dict.get(value) is not None:
                return [dict[value], index]

            dict[target - value] = index

        