class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        self.offset = self.find_offset(nums)
        self.size = len(nums)

        l, r = 0, len(nums)-1
        while l <= r:
            mid_index = (r-l)//2 + l
            mid_num = nums[self.cvt_i(mid_index)]
            if mid_num < target:
                l = mid_index + 1
            elif mid_num > target:
                r = mid_index - 1
            elif mid_num == target:
                return self.cvt_i(mid_index)
        
        return -1

    def find_offset(self, nums: List[int]) -> int:
        first_item = nums[0]
        l, r = 0, len(nums)-1
        while r - l > 1:
            mid_index = (r-l)//2 + l
            if nums[mid_index] < first_item:
                r = mid_index
            elif nums[mid_index] > first_item:
                l = mid_index
        
        if nums[l] > nums[r]:
            return r
        else:
            return 0

    def cvt_i(self, index: int):
        return (index + self.offset) % self.size
    
def main():
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    s.search(nums, 0)

if __name__ == "__main__":
    main()