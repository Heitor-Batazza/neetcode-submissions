class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 1
        set_s = list(set(s))
        for x in range(0, len(set_s)):
            base = set_s[x]
            for y in range(0, len(s)):
                base_k = k
                contador = 0
                for z in range(y, len(s)):
                    if s[z] == base:
                        contador += 1
                    elif base_k > 0:
                        contador += 1
                        base_k -= 1
                    else:
                        break
                output = max(output, contador)
        return output

