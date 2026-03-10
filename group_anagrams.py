class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}
        res = []

        for s in strs:
            ordered_s = "".join(sorted(s))
            if ordered_s not in anagram_groups:
                anagram_groups[ordered_s] = []
            anagram_groups[ordered_s].append(s)
        
        for ordered_s in anagram_groups:
            res.append(anagram_groups[ordered_s])
        
        return res