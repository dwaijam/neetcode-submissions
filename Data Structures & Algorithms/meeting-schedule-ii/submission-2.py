"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: [x.start, x.end])
        print(intervals)
        minheap = []
        for inter in intervals:
            print(inter)
            if minheap and minheap[0]<=inter.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, inter.end)

        return len(minheap)