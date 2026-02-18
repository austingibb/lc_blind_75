class Solution:
    def findMin(self, nums: List[int]) -> int:
        first_item = nums[0]
        l, r = 0, len(nums) - 1
        while r - l > 1:
            mid = (r-l)//2+l
            if nums[mid] > first_item:
                l = mid
            elif nums[mid] < first_item:
                r = mid
            
        if nums[l] > nums[r]:
            return nums[r]
        else:
            return first_item