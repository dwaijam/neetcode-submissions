class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        visited = set()
        visited.add(0)
        for i in range(1, len(points)):
            point = points[i]
            heapq.heappush(minheap, (abs(point[0] - points[0][0]) + abs(point[1] - points[0][1]),i))

        res = 0
        while minheap and len(visited) < len(points):
            dis, pop =  heapq.heappop(minheap)
            if pop not in visited:
                res+=dis
                visited.add(pop)
                for i in range(1, len(points)):
                    if i not in visited:
                        point = points[i]
                        heapq.heappush(minheap, (abs(point[0] - points[pop][0]) + abs(point[1] - points[pop][1]),i))

        return res
            



