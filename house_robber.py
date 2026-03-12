class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cache = {}
        return self.rob_recurse(0, nums)

    def rob_recurse(self, i, nums):
        if i >= len(nums):
            return 0
        
        if i in self.cache:
            return self.cache[i]
        
        total = max(nums[i] + self.rob_recurse(i+2, nums), self.rob_recurse(i+1, nums))

        self.cache[i] = total
        return total
        