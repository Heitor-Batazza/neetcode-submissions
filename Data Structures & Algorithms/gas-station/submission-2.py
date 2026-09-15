class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif = [l - r for l, r in zip(gas, cost)]
        l = 0
        length = len(dif)

        if sum(dif) < 0:
            return -1

        while True:
            total = 0
            for r in range(l, l + length):
                r_cor = r % length
                if r == l + length - 1:
                    return l
                elif (total + dif[r_cor]) > 0:
                    total += dif[r_cor]
                else:
                    break
            l += 1

