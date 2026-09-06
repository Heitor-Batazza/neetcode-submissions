class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicionario_s = {}
        dicionario_t = {}

        for i in range(0, len(s)):
            dicionario_s[s[i]] = 1 + dicionario_s.get(s[i], 0)
        for j in range(0, len(t)):
            dicionario_t[t[j]] = 1 + dicionario_t.get(t[j], 0)
        
        if dicionario_s == dicionario_t:
            return True
        else:
            return False