class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = defaultdict(list)
        for f in flights:
            routes[f[0]].append((f[1], f[2]))

        q = deque()
        q.append(src)
        minheap = []
        heapq.heappush(minheap, (0, src, 0))
        while minheap:
            print(minheap)
            price, node, hop = heapq.heappop(minheap)
            if node == dst and hop <= k+1:
                return price
            for nei in routes[node]:
                heapq.heappush(minheap, (price+nei[1], nei[0], hop+1))
            
            
        return -1