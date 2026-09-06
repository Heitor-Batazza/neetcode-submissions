class Solution:
    def isValid(self, s: str) -> bool:
        dicionario = {"{": "}", "}": "{", "[": "]", "]": "[", "(": ")", ")": "("}
        inicio = ("{", "[", "(")
        i = -1
        lista_s = list(s)

        if (len(s) % 2) == 1:
            return False


        while lista_s != []:
            i += 1
            if lista_s[i] in inicio and dicionario[lista_s[i]] == lista_s[i + 1]:
                lista_s.pop(i)
                lista_s.pop(i)
                i = -1
            elif i == len(lista_s) - 2:
                return False
        return True
        
            
