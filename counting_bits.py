class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            ans.append(self.bits_in_int(i))
        return ans
    
    @staticmethod
    def bits_in_int(i):
        count = 0
        while i > 0:
            if i & 1:
                count += 1
            i = i >> 1
        return count
        