from functools import reduce  
from operator import xor  

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.missingNumberXor(nums)

    def missingNumberSum(self, nums: List[int]) -> int:
        n=len(nums)
        return int(n*(n+1)/2) - sum(nums)

    def missingNumberXor(self, nums: List[int]) -> int:
        numsXor = reduce(xor, nums)
        fullXor = reduce(xor, range(0, len(nums)+1))
        return numsXor ^ fullXor 