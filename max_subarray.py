class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.linear(nums)

    def linear(self, nums):
        global_max = float("-inf")
        cur_max = float("-inf")
        for n in nums:
            cur_max = max(n, n+cur_max)
            global_max = max(global_max, cur_max)
        return global_max
        