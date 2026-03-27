class Solution(object):
    OPENING_PARENTHESES = "{[("
    CLOSING_PARENTHESES = "}])"
    PARENTHESES = OPENING_PARENTHESES + CLOSING_PARENTHESES

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = deque()
        for c in s:
            if c not in Solution.PARENTHESES:
                return False
            elif c in Solution.OPENING_PARENTHESES:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                if self.sameType(stack[-1], c):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

    @staticmethod
    def sameType(c1, c2):
        curly = "\{\}"
        open_brackets = "()"
        square = "[]"

        if c1 in curly and c2 in curly:
            return True
        
        if c1 in open_brackets and c2 in open_brackets:
            return True
        
        if c1 in square and c2 in square:
            return True

        return False