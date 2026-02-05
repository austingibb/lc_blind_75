class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    
def main():
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.canJump(nums))


if __name__ == "__main__":
    main()