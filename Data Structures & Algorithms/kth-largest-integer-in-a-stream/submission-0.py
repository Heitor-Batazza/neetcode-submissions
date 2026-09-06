class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        (self.nums).append(val)
        (self.nums).sort()
        length = len(self.nums)
        return self.nums[length - self.k]
        
