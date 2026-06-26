class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        qs = sorted(queries)
        minheap = []
        i = 0
        res = {}
        for q in qs:
            while i< len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minheap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1] ))
                i+=1
           
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if not minheap:
                res[q] = -1
            else:
                res[q] = minheap[0][0]
        ans = []
        for q in queries:
            ans.append(res[q])
        return ans
            
        

            

            
