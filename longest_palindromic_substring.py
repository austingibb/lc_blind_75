'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: strr
        """
        return self.iterativeSpread(s)
        
    def iterativeSpread(self, s):
        max_width = 0
        max_index = -1
        s = '#' + '#'.join(s) + '#'
        for i in range(0, len(s)):
            width = 0
            while i - width >= 0 and i + width < len(s) and s[i-width] == s[i+width]:
                width += 1
            width -= 1
            if max_width < width:
                max_width = width
                max_index = i
            
        return s[max_index-max_width:max_index+max_width].replace("#", "")
    
def main():
    sol = Solution()
    res = sol.longestPalindrome("babad")   
    print(res)

if __name__ == "__main__":
    main() 