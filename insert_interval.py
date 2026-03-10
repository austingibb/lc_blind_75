class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # go through intervals, find which overlap with new interval, establish new interval left and right positions merging in each interval
        # save indicies of merged intervals
        # remove every saved index, then insert at leftmost saved index
        return self.insert_clean(intervals, newInterval)

    def insert_clean(self, intervals, newInterval):
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        res.append(newInterval)
        return res


    def insert_naive(self, intervals, newInterval):
                # go through intervals, find which overlap with new interval, establish new interval left and right positions merging in each interval
        # save indicies of merged intervals
        # remove every saved index, then insert at leftmost saved index
        merged_left = newInterval[0]
        merged_right = newInterval[1]
        overlapping_idx = []
        insertion_index_non_overlapping = -1

        for index, interval in enumerate(intervals):
            left, right = interval[0], interval[1]
            if self.is_overlapping(left, right, merged_left, merged_right):
                merged_left = min(left, merged_left)
                merged_right = max(right, merged_right)
                overlapping_idx.append(index)
            if insertion_index_non_overlapping == -1 and left > merged_left:
                insertion_index_non_overlapping = index

        if insertion_index_non_overlapping == -1:
            insertion_index_non_overlapping = len(intervals)

        if len(overlapping_idx) > 0:
            insertion_idx = overlapping_idx[0]
            del intervals[insertion_idx:(insertion_idx+len(overlapping_idx))]
            intervals.insert(insertion_idx, [merged_left, merged_right])
        else:
            intervals.insert(insertion_index_non_overlapping, [merged_left, merged_right])
        
        return intervals

    @staticmethod
    def is_overlapping(i1_left, i1_right, i2_left, i2_right):
        # i1 has left or right within i2 bounds and vice versa
        return (i2_left <= i1_left and i1_left <= i2_right) or (i2_left <= i1_right and i1_right <= i2_right) \
        or (i1_left <= i2_left and i2_left <= i1_right) or (i1_left <= i2_right and i2_right <= i1_right)