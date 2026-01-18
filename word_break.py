class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(s_idx: int) -> bool:
            if s_idx in cache:
                return cache[s_idx]
            
            if s_idx == len(s):
                return True
            
            result = False
            for word in wordDict:
                index_of_word = s.find(word, s_idx)
                if index_of_word == s_idx:
                    result = result or dfs(s_idx+len(word))
            
            cache[s_idx] = result
            return result

        return dfs(0)
    

def main():
    s = Solution()
    s.wordBreak("leetcode", ["leet", "code"])

if __name__ == "__main__":
    main()