class Solution:
    def climbStairs(self, n: int) -> int:
        list = [1, 1]

        for _ in range(n - 1):
            list.append(sum(list))
            list.pop(0)

        return list[1]