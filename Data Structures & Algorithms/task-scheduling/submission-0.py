class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        dic = Counter(tasks)
        q = deque()
        maxheap = []
        for task, freq in dic.items():
            heapq.heappush(maxheap, (-freq,task))
        
        count = 0
        while maxheap or q:
            if maxheap:
                _, task = heapq.heappop(maxheap)
                count+=1
                dic[task]-=1
                print(task, count)
                if dic[task] > 0:
                    q.append((count+n, task))
            else:
                count = q[0][0]
            if q:
                while q and q[0][0]<=count:
                    count, task = q.popleft()
                    if dic[task] >=1:
                        heapq.heappush(maxheap, (-dic[task],task))

        return count
