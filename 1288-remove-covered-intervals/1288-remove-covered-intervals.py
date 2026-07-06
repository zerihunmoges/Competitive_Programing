class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], -x[1]))

        new_interval= [intervals[0]]
        for i in range(1, len(intervals)):

            start, end = intervals[i]
            p_start, p_end = new_interval[-1]
            if not (p_start <= start and p_end >= end):
                 new_interval.append([start, end])


        return len(new_interval)
        