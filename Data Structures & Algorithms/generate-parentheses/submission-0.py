class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(subset, openings, endings):
            if openings == 0 and endings == 0:
                res.append(subset)
                return

            if openings > 0:
                subset = subset + "("
                dfs(subset, openings - 1, endings + 1)
                subset = subset[:-1]

            if endings > 0:
                subset = subset + ")"
                dfs(subset, openings, endings - 1)

        dfs("", n, 0)

        return res
        