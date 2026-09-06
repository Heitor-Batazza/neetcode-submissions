class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        contagem_s1 = {}
        output = False

        for caractere in s1:
            contagem_s1[caractere] = contagem_s1.get(caractere, 0) + 1

        for i in range(0, (s2_length - s1_length + 1)):
            contagem_s2 = {}
            s2_slice = s2[i:(i + s1_length)]
            for caractere in s2_slice:
                contagem_s2[caractere] = contagem_s2.get(caractere, 0) + 1
            if contagem_s2 == contagem_s1:
                output = True
        return output
