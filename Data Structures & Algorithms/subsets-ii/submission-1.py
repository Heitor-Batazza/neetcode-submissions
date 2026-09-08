class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i, subset, res):
            if (i == len(nums)) and (subset not in res):
                res.append(subset.copy())
                return
            elif (i == len(nums)) and (subset in res):
                return

            subset.append(nums[i])
            dfs(i + 1, subset, res)

            subset.pop()
            dfs(i + 1, subset, res)

        dfs(0, subset, res)

        return res




        