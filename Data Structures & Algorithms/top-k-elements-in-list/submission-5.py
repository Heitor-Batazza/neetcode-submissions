class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #números = []
        #for i in range(len(nums)):
        #    if nums[i] not in números:
        #        números.append(nums[i])

        números = list(set(nums))

        quantidade = [0] * (len(números))
        for i in range(len(nums)):
            for j in range(len(números)):
                if nums[i] == números[j]:
                    quantidade[j] += 1

        output = []
        for i in range(0, k):
            index = quantidade.index(max(quantidade))
            
            output.append(números[index])
            quantidade[index] = 0
        
        return output

