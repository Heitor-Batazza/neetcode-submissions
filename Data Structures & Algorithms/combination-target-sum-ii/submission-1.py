class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            cur.pop()
            if i >= (len(candidates) - 1):
                    return
            while candidates[i + 1] == candidates[i]:
                i += 1
                if i >= (len(candidates) - 1):
                    return
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
        