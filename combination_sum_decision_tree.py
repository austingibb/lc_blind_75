import math

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.recurse_candidate(0, candidates, 0, [], target, result)
        return result

    def recurse_candidate(self, index: int, candidates: List[int], current_sum: int, combination: List, target: int, result: List):
        if index == len(candidates):
            return
        if current_sum == target:
            result.append(combination.copy())
            return
        elif current_sum > target:
            return

        # move on from current candidate
        self.recurse_candidate(index + 1, candidates, current_sum, combination, target, result)

        candidate = candidates[index]
        # add one more of current candidate
        current_sum += candidate
        combination.append(candidate)
        self.recurse_candidate(index, candidates, current_sum, combination, target, result)
        del combination[-1:]
        current_sum -= candidate
        
            
def main():
    candidates = [2,3,5]
    target = 8
    s = Solution()
    s.combinationSum(candidates, target)   

if __name__ == "__main__":
    main()