class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        s1_sorted = sorted(s1)

        for i in range(0, (s2_length - s1_length + 1)):
            contagem_s2 = {}
            s2_slice = s2[i:(i + s1_length)]
            s2_slice_sorted = sorted(s2_slice)
            if s1_sorted == s2_slice_sorted:
                return True
        return False
