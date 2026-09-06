class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(0, len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if j == (len(temperatures) - 1) and temperatures[i] >= temperatures[j]:
                    output += [0]
                elif temperatures[j] > temperatures[i]:
                    output += [j - i]
                    break
        output += [0]
        return output

        