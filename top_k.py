class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        for n in nums:
            if n not in frequency:
                frequency[n] = 0
            frequency[n] += 1
        
        # sort by most frequent
        sorted_items = sorted(frequency.items(), reverse=True, key=lambda item: item[1])
        # remove tuple and frequency information now that it is sorted
        most_frequent = [n for n, freq in sorted_items]
        # return top k from sorted based on frequency
        return most_frequent[0:k]
        