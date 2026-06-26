class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        res = []
        if not intervals:
            return [ni]
        ns = float('inf')
        ne = float('-inf')
        first = intervals[0]
        last = intervals[-1]
        if ni[1] < first[0]:
            intervals.insert(0, ni)
            return intervals
        elif ni[0] > last[1]:
            intervals.append(ni)
            return intervals

            
        inserted = False
        ms = ni[0]
        me = ni[1]
        for st,en in intervals:
            if en < ni[0]:
                res.append([st,en])
                continue
            if st > me:
                if not inserted:
                    res.append([ms,me])
                    inserted = True
                res.append([st,en])
            else:
                ms = min(ms, st)
                me = max(me, en)

        if not inserted:
            res.append([ms,me])

        return res