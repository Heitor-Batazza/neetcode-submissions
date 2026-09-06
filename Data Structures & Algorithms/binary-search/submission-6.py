class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1

        length = len(nums)

        dict = {elemento: indice for indice, elemento in enumerate(nums)}

        while True:
            if target > nums[int((length/2))]:
                for i in range(int((length/2))):
                    nums.pop(0)
                length = len(nums)

            elif target < nums[int((length/2))]:
                for i in range(int((length/2))):
                    nums.pop()
                length = len(nums)

            else:
                return dict[nums[int((length/2))]]
        