class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach_idx = [False for num in nums]
        can_reach_idx[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            can_reach = False
            for j in range(1, nums[i]+1):
                if i + j < len(nums):
                    can_reach = can_reach or can_reach_idx[i+j]
                else:
                    break
            can_reach_idx[i] = can_reach
        
        return can_reach_idx[0]
    
def main():
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.canJump(nums))


if __name__ == "__main__":
    main()