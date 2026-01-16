import math

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidate_max_multiplier = [math.floor(target/c) for c in candidates]
        self.recurse_candidate(0, candidates, 0, [], target, candidate_max_multiplier, result)
        return result

    def recurse_candidate(self, index: int, candidates: List[int], current_sum: int, combination: List, target: int, candidate_max_multiplier: List[int], result: List):
        if current_sum == target:
            result.append(combination.copy())
            return
        
        if index == len(candidates):
            return
        candidate = candidates[index]

        for multiplier in range(0, candidate_max_multiplier[index]+1):
            combination.extend([candidate] * multiplier)
            current_sum += candidate * multiplier
            if current_sum <= target:
                self.recurse_candidate(index+1, candidates, current_sum, combination, target, candidate_max_multiplier, result)
            # reset sum and remove added elements
            current_sum -= candidate * multiplier
            if multiplier > 0:
                del combination[-multiplier:]
            
def main():
    candidates = [2,3,5]
    target = 8
    s = Solution()
    s.combinationSum(candidates, target)   

if __name__ == "__main__":
    main()