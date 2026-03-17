class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if not s:
            return 0
       
        l, r = 0, 0
        longest = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            cur_len = r-l+1
            if cur_len > longest:
                longest = cur_len

        return longest 