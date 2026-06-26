class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxheap = []
        def euclidean_distance(x1, y1):
            return math.sqrt((x1) ** 2 + (y1) ** 2)

        for point in points:
            heapq.heappush(maxheap, (-euclidean_distance(point[0], point[1]), point))
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return [x[1] for x in maxheap]