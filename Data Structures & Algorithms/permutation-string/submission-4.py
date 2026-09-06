class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        for caractere in s1:
            count_s1[caractere] = count_s1.get(caractere, 0) + 1

        for i in range(0, (len(s2) - len(s1) + 1)):
            s2_slice = s2[i:(i + len(s1))]

            count_s2_slice = {}
            for caractere in s2_slice:
                count_s2_slice[caractere] = count_s2_slice.get(caractere, 0) + 1

            if count_s1 == count_s2_slice:
                return True
        return False
