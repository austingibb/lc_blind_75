class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cache = { len(s): 1 }
        return self.num_decodings_recursive(s, 0)
    
    def num_decodings_recursive(self, s, i):
        if i in self.cache:
            return self.cache[i]

        char = s[i]
        if char == '0':
            self.cache[i] = 0
            return 0

        num_ways = 0
        remaining_chars = len(s) - i
        if remaining_chars >= 2:
            single_char_ways = self.num_decodings_recursive(s, i+1)
            if int(s[i:i+2]) <= 26:
                double_char_ways = self.num_decodings_recursive(s, i+2)
            else:
                double_char_ways = 0
            num_ways = single_char_ways + double_char_ways
        elif remaining_chars == 1:
            num_ways = 1
        
        self.cache[i] = num_ways
        return num_ways
