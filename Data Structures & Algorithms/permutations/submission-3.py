class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(nums, subset, res):
            if len(nums) == 1:
                subset.append(nums[0])
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                nums_copy = nums.copy()
                subset_copy = subset.copy()

                subset.append(nums[i])
                removed_value = nums.pop(i)
                dfs(nums, subset.copy(), res)

                nums = nums_copy
                subset = subset_copy

        dfs(nums, subset, res)
        return res

            

        