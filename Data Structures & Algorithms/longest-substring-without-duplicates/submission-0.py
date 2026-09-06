class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        for i in range(0, len(s)):
            suporte = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in suporte:
                    suporte += s[j]
                else:
                    break
            output = max(output, len(suporte))
        return output
                
        