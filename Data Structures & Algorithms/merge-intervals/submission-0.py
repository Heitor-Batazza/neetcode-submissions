class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        i = 0

        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                newInterval = [[intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]]
                intervals.pop(i)
                intervals.pop(i)
                intervals = intervals[:i] + newInterval + intervals[i:]
            else:
                i += 1

        return intervals
                