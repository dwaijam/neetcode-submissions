class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-num for num in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>0:
            if len(maxheap) == 1:
                return -maxheap[0]
            a = heapq.heappop(maxheap)
            b = heapq.heappop(maxheap)
            heapq.heappush(maxheap, -abs(a-b))
        
        return 0