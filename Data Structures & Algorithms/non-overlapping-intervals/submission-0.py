class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))

        st,en = intervals[0]
        count = 0
        for inter in intervals[1:]:
            if inter[0]<en: #merge
                count+=1
                if inter[1] < en:
                    st,en = inter
            else:
                st,en = inter

        return count
