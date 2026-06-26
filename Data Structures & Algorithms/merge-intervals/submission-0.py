class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.append([float('inf'), float('inf')])
        intervals.sort(key=lambda x: x[0])
        st, en = intervals[0]
        res = []
        for inter in intervals[1:]:
            if inter[0] > en:
                res.append([st, en])
                st = inter[0]
                en = inter[1]
            else:
                en = max(en,  inter[1])

        return res


