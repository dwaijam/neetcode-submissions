class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)

        l = 1
        r = mx

        while l<r:
            mid = (l+r)//2
            hours_taken = 0
            for p in piles:
                hours_taken+=math.ceil(p/mid)
             
            if hours_taken > h:
                l = mid + 1
            else:
                r = mid

        return l        

        