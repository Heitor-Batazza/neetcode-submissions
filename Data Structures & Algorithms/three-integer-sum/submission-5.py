class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        i = 0

        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            target = -nums[i]

            while l < r:
                sum = nums[l] + nums[r]

                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
            while (i < len(nums) - 2) and (nums[i] == nums[i + 1]):
                i += 1
            i += 1
        return output

                




        