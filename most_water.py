class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # area = min(height[i], height[j]) * (j-i)
        # naive, try every pair of lines, n^2
        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area