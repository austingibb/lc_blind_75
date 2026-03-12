class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rob_linear(nums)

    def rob_linear(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            cur_rob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = cur_rob
        return cur_rob

    def rob_n_cache(self, nums):
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