class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_atualizado = s.replace(" ", "").lower()
        s_atualizado = re.sub(r'[^a-zA-Z0-9]', '', s_atualizado)
        
        output = True
        for i in range(0, len(s_atualizado)):
            j = len(s_atualizado) - (i + 1)
            if s_atualizado[i] != s_atualizado[j]:
                output = False
        return output