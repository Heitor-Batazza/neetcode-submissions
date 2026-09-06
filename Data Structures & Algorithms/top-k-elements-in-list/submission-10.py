class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contagem = {}
        output = []
        nums_unicos = list(set(nums))

        for caractere in nums:
            contagem[caractere] = 1 + contagem.get(caractere, 0)
        print(contagem)
        print(contagem[nums_unicos[0]])
        for j in range(0, k):
            base = 0
            for i in range(0, len(nums_unicos)):
                if contagem[nums_unicos[i]] >= base:
                    base = contagem[nums_unicos[i]]
                    index = i
            output.append(nums_unicos[index])
            contagem[nums_unicos[index]] = 0

        return output

