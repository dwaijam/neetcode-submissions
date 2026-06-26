class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap = []
        gr = defaultdict(list)
        for u, v, w in times:
            gr[u].append((v, w))
        dis = [float('inf')] * (n+1)
        dis[k] = 0

        minheap.append((0, k))
        while minheap:
            dist, node = heapq.heappop(minheap)
            if dist > dis[node]:
                continue
            
            for neighbor, time in gr[node]:
                distance = dist + time
                if distance < dis[neighbor]:
                    dis[neighbor] = distance
                    heapq.heappush(minheap, (distance, neighbor))

        ans = max(dis[1:])
        if ans < float('inf'):
            return ans
        else:
            return -1


        
        