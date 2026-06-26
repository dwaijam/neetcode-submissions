class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mxheap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(mxheap, (-nums[i], i))
            if i >= k-1:
                while mxheap[0][1] <= i-k:
                    heapq.heappop(mxheap)
                res.append(-mxheap[0][0])
        return res


        