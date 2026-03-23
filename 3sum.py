class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        i = 0
        prev = None
        while i < len(nums)-2:
            num = nums[i]
            
            if not prev or prev != num:
                l, r = i+1, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] + num > 0:
                        r -= 1    
                    else:
                        if nums[l] + nums[r] + num == 0:
                            res.append([num, nums[l], nums[r]])
                        
                        while True:
                            l += 1
                            if nums[l-1] != nums[l] or l >= r:
                                break
                    
            prev = num
            i += 1
            
        return res
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))