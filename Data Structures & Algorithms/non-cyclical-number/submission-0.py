class Solution:
    def isHappy(self, n: int) -> bool:
        list_values = [n]

        def sum_squares(string_n):
            new_n = 0
            for i in string_n:
                new_n += (int(i))**2
            return new_n
        
        while n != 1:
            n = sum_squares(str(n))
            if n in list_values:
                return False
            else:
                list_values.append(n)

        return True

        