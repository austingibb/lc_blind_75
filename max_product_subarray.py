class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max(nums)
        max_ending_at_i = 1
        min_ending_at_i = 1
        for n in nums:
            if n == 0:
                max_ending_at_i = 1
                min_ending_at_i = 1
                continue
            
            tmp_max_ending_at_i = max_ending_at_i
            max_ending_at_i = max(n * max_ending_at_i, n * min_ending_at_i, n)
            min_ending_at_i = min(n * min_ending_at_i, n * tmp_max_ending_at_i, n)
            global_max = max(global_max, max_ending_at_i)
        return global_max