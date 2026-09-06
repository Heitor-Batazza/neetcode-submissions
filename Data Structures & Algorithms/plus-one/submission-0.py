class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_list = ""
        output = []

        for element in digits:
            string_list += str(element)

        new_string_list = str(int(string_list) + 1)
        
        for element in new_string_list:
            output.append(int(element))

        return output   