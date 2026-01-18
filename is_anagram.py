class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s.lower())) == "".join(sorted(t.lower()))