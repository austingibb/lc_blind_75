class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums = sorted(nums)
        max_seq = 1
        cur_seq = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num == prev + 1:
                cur_seq += 1
            elif num == prev:
                continue
            else:
                cur_seq = 1
            max_seq = max(cur_seq, max_seq)
            prev = num
        return max_seq