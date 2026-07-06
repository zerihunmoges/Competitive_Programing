class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], -x[1]))

        p_start, p_end= intervals[0]
        count = 1
        for i in range(1, len(intervals)):

            start, end = intervals[i]
            if not (p_start <= start and p_end >= end):
                 p_start, p_end=[start, end]
                 count += 1

        return count
        