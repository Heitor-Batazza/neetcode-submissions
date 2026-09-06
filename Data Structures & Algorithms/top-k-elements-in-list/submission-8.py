class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numeros_unicos = list(set(nums))

        quantidade = [0] * (len(numeros_unicos))
        for i in range(len(nums)):
            for j in range(len(numeros_unicos)):
                if nums[i] == numeros_unicos[j]:
                    quantidade[j] += 1

        output = []
        for i in range(0, k):
            index = quantidade.index(max(quantidade))
            
            output.append(numeros_unicos[index])
            quantidade[index] = 0
        
        return output

