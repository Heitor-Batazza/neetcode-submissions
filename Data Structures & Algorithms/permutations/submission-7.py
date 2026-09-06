class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs():
            if len(nums) == 0:
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                subset.append(nums[i])
                removed_value = nums.pop(i)

                dfs()

                subset.pop()
                nums.insert(i, removed_value)

        dfs()
        return res

            

        