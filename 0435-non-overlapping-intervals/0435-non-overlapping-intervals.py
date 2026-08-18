class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        result = 0
        prevend = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                result += 1
                prevend = min(end , prevend)
        return result
        